from ..learner import Learner
from ..policies import RandomPolicy
from ..util import max_action_value
from ..value_functions import TabularF
from ...utils import check_random_state


class QLearning(Learner):

    def __init__(self, env, policy=None, qf=None, learning_rate=0.1,
                 discount_factor=0.99, n_episodes=1000, random_state=None,
                 verbose=None):
        super(QLearning, self).__init__(env, n_episodes=n_episodes, verbose=verbose)
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.random_state = check_random_state(random_state)
        self.policy = policy or RandomPolicy(env.actions, self.random_state)
        self.qf = qf or TabularF(self.random_state)

    def best_qvalue(self, state):
        return max_action_value(self.qf, state, self.env.actions(state))

    ###########
    # Learner #
    ###########

    def episode(self):
        while not self.env.is_terminal():
            state = self.env.cur_state()
            action = self.policy.action(state)
            reward, next_state = self.env.do_action(action)
            best_qvalue = self.best_qvalue(next_state)
            target = reward + (self.discount_factor * best_qvalue)
            td_error = target - self.qf[state, action]
            self.qf[state, action] += self.learning_rate * td_error
