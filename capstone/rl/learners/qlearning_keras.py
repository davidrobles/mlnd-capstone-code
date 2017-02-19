from ..policies import RandomPolicy
from ..tabularf import TabularF
from ..util import max_action_value
from ...utils import check_random_state


class QLearningKeras(object):

    def __init__(self, env, policy=None, qf=None, alpha=0.1, gamma=0.99,
                 n_episodes=1000, random_state=None, verbose=True):
        self.env = env
        self.alpha = alpha
        self.gamma = gamma
        self.n_episodes = n_episodes
        self.random_state = check_random_state(random_state)
        self.policy = policy or RandomPolicy(self.random_state)
        self.qf = qf or TabularF(self.random_state)
        self.verbose = verbose
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
            value = self.qf.get_value(s)
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
        if self.verbose:
            print('Episode {self.cur_episode} / {self.n_episodes}'.format(self=self))
        self.env.reset()
        while not self.env.is_terminal():
            self.step()
        self.cur_episode += 1

    def step(self):
        state, actions = self.env.cur_state_and_actions()
        action = self.policy.action(state, actions, self.qf)
        reward, next_state, next_actions = self.env.do_action(action)
        if next_state.is_over():
            update = reward
        else:
            best_action_value = self.get_max(next_state)
            update = reward + (self.gamma * best_action_value)
        assert update >= -1.0 and update <= 1.0
        self.qf.update(state, update)
