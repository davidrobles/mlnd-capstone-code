from ..learner import Learner
from ..policies import RandomPolicy
from ..value_functions import TabularF
from ...utils import check_random_state


class Sarsa(Learner):

    def __init__(self, env, policy=None, qf=None, alpha=0.1, gamma=0.99,
                 n_episodes=1000, random_state=None, verbose=None):
        super(Sarsa, self).__init__(env, n_episodes=n_episodes, verbose=verbose)
        self.policy = policy
        self.alpha = alpha
        self.gamma = gamma
        self.random_state = check_random_state(random_state)
        self.policy = policy or RandomPolicy(env.actions, self.random_state)
        self.qf = qf or TabularF(self.random_state)

    ###########
    # Learner #
    ###########

    def episode(self):
        state = self.env.cur_state()
        action = self.policy.action(state)
        while not self.env.is_terminal():
            reward, next_state = self.env.do_action(action)
            next_action = self.policy.action(next_state)
            td_error = reward + (self.gamma * self.qf[next_state, next_action]) - self.qf[state, action]
            self.qf[state, action] += self.alpha * td_error
            state, action = next_state, next_action
