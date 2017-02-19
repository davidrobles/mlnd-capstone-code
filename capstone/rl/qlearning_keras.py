
import numpy as np
import random
from .tabularf import TabularF
from .util import max_action_value
from ..policy import RandomPolicy
from ..utils import check_random_state
from ..utils import normalize_board


class QLearningKeras(object):

    def __init__(self, env, policy=None, qf=None, alpha=0.1, gamma=0.99,
                 n_episodes=1000, random_state=None):
        self.env = env
        self.alpha = alpha
        self.gamma = gamma
        self.n_episodes = n_episodes
        self.random_state = check_random_state(random_state)
        self.policy = policy or RandomPolicy(self.random_state)
        self.qf = qf or TabularF(self.random_state)
        self.cur_episode = 1

    def best_action_value(self, state, actions):
        return max_action_value(self.qf, state, actions)

    def learn(self):
        for _ in range(self.n_episodes):
            self.episode()

    def get_max(self, state):
        # best = -1000000 if state.cur_player() == 0 else 1000000
        best = -1000000
        assert state.cur_player() == 0
        for action in state.legal_moves():
            s = state.copy()
            s = s.make_move(action)
            value = self.qf.model.predict(normalize_board(s.board), batch_size=1)
            assert value >= -1.0 and value <= 1.0
            if value > best:
                best = value
            # if state.cur_player() == 0:
            #     if value > best:
            #         best = value
            # else:
            #     if value < best:
            #         best = value
        return best

    def episode(self):
        print('Episode {self.cur_episode} / {self.n_episodes}'.format(self=self))
        self.env.reset()
        step = 1

        while not self.env.is_terminal():
            # print('  Step %d' % step)
            state, actions = self.env.cur_state_and_actions()
            # qval = self.qf.model.predict(self.convert(state), batch_size=1)
            # action = self.policy.action(state, actions, self.qf)
            import random
            action = random.choice(actions)
            if action is None:
                import pdb; pdb.set_trace()
            reward, next_state, next_actions = self.env.do_action(action)
            y = np.zeros((1, 1))
            if next_state.is_over():
                y[0][0] = reward
            else:
                best_action_value = self.get_max(next_state)
                t = reward + (self.gamma * best_action_value)
                assert t > -1.0 and t < 1.0
                y[0][0] = t
            self.qf.model.fit(normalize_board(state.board), y, batch_size=1, nb_epoch=1, verbose=0)
            step += 1
        self.cur_episode += 1
