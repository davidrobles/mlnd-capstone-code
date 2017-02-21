from ..learner import Learner
from ..policies import RandomPolicy
from ..value_functions import TabularF
from ..util import max_action_value
from ...utils import check_random_state


class ApproximateQLearning(Learner):

    def __init__(self, env, qf, policy=None, discount_factor=0.99,
                 n_episodes=1000, random_state=None, verbose=True):
        super(ApproximateQLearning, self).__init__(env, n_episodes=n_episodes, verbose=verbose)
        self.discount_factor = discount_factor
        self.random_state = check_random_state(random_state)
        self.policy = policy or RandomPolicy(env.actions, random_state=self.random_state)
        self.qf = qf

    def best_action_value(self, state, actions):
        return max_action_value(self.qf, state, actions)

    def get_max(self, state):
        if state.is_over():
            return 0
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

    ###########
    # Learner #
    ###########

    def episode(self):
        while not self.env.is_terminal():
            state = self.env.cur_state()
            action = self.policy.action(state)
            reward, next_state = self.env.do_action(action)
            best_qvalue = self.get_max(next_state)
            update = reward + (self.discount_factor * best_qvalue)
            self.qf.update(state, update)
