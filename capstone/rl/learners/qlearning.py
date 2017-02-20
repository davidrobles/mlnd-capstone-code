from ..learner import Learner
from ..policies import RandomPolicy
from ..util import max_action_value
from ..value_functions import TabularF
from ...utils import check_random_state


class QLearning(Learner):

    def __init__(self, env, policy=None, qf=None, alpha=0.1, gamma=0.99,
                 n_episodes=1000, random_state=None, verbose=None):
        super(QLearning, self).__init__(env, n_episodes=n_episodes, verbose=verbose)
        self.alpha = alpha
        self.gamma = gamma
        self.random_state = check_random_state(random_state)
        self.policy = policy or RandomPolicy(env.actions, self.random_state)
        self.qf = qf or TabularF(self.random_state)

    def best_action_value(self, state, actions):
        return max_action_value(self.qf, state, actions)

    ###########
    # Learner #
    ###########

    def episode(self):
        while not self.env.is_terminal():
            state, actions = self.env.cur_state_and_actions()
            action = self.policy.action(state)
            reward, next_state, next_actions = self.env.do_action(action)
            best_action_value = self.best_action_value(next_state, next_actions)
            td_error = reward + (self.gamma * best_action_value) - self.qf[state, action]
            self.qf[state, action] += self.alpha * td_error
