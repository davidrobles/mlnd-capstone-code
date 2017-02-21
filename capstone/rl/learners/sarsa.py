from ..learner import Learner
from ..policies import RandomPolicy
from ..value_functions import TabularQ
from ...utils import check_random_state


class Sarsa(Learner):

    def __init__(self, env, policy=None, learning_rate=0.1, discount_factor=0.99,
                 n_episodes=1000, verbose=True, random_state=None):
        super(Sarsa, self).__init__(env, n_episodes=n_episodes, verbose=verbose)
        self.policy = policy
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.random_state = check_random_state(random_state)
        self.policy = policy or RandomPolicy(env.actions, random_state=self.random_state)
        self.qf = TabularQ(random_state=self.random_state)

    ###########
    # Learner #
    ###########

    def episode(self):
        state = self.env.cur_state()
        action = self.policy.action(state)
        while not self.env.is_terminal():
            reward, next_state = self.env.do_action(action)
            next_action = self.policy.action(next_state)
            target = reward + (self.discount_factor * self.qf[next_state, next_action])
            td_error = target - self.qf[state, action]
            self.qf[state, action] += self.learning_rate * td_error
            state, action = next_state, next_action
