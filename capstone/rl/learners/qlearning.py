from ..learner import Learner
from ..policies import RandomPolicy
from ..utils import max_qvalue
from ..value_functions import TabularQ
from ...utils import check_random_state


class QLearning(Learner):
    '''Tabular Q-learning'''

    def __init__(self, env, policy=None, learning_rate=0.1, discount_factor=0.99,
                 random_state=None, **kwargs):
        super(QLearning, self).__init__(env, **kwargs)
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.random_state = check_random_state(random_state)
        self.policy = policy or RandomPolicy(env.actions, random_state=self.random_state)
        self.qf = TabularQ(random_state=self.random_state)

    def best_qvalue(self, state):
        return max_qvalue(state, self.env.actions(state), self.qf)

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


class ApproximateQLearning(Learner):
    '''Q-learning with a function approximator'''

    def __init__(self, env, qf, policy=None, discount_factor=0.99, random_state=None, **kwargs):
        super(ApproximateQLearning, self).__init__(env, **kwargs)
        self.qf = qf
        self.discount_factor = discount_factor
        self.random_state = check_random_state(random_state)
        self.policy = policy or RandomPolicy(env.actions, random_state=self.random_state)

    def best_qvalue(self, state, actions):
        return max_qvalue(state, actions, self.qf)

    ###########
    # Learner #
    ###########

    def episode(self):
        while not self.env.is_terminal():
            state = self.env.cur_state()
            action = self.policy.action(state)
            reward, next_state = self.env.do_action(action)
            next_actions = self.env.actions(next_state)
            best_qvalue = self.best_qvalue(next_state, next_actions)
            update = reward + (self.discount_factor * best_qvalue)
            self.qf.update(state, update)
