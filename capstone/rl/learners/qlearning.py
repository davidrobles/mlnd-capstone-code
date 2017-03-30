import random
from collections import deque
from ..learner import Learner
from ..utils import max_qvalue


class QLearning(Learner):
    '''Tabular Q-learning'''

    def __init__(self, env, policy, qfunction, learning_rate=0.1,
                 discount_factor=1.0, **kwargs):
        super(QLearning, self).__init__(env, **kwargs)
        self.policy = policy
        self.qfunction = qfunction
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor

    def best_qvalue(self, state):
        return max_qvalue(state, self.env.actions(state), self.qfunction)

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
            td_error = target - self.qfunction[state, action]
            self.qfunction[state, action] += self.learning_rate * td_error


class ApproximateQLearning(Learner):
    '''Q-learning with a function approximator'''

    def __init__(self, env, policy, qfunction, discount_factor=1.0,
                 experience_replay=True, **kwargs):
        super(ApproximateQLearning, self).__init__(env, **kwargs)
        self.policy = policy
        self.qfunction = qfunction
        self.discount_factor = discount_factor
        self.experience_replay = experience_replay
        if self.experience_replay:
            self.memory = deque(maxlen=10000)

    def best_qvalue(self, state):
        return max_qvalue(state, self.env.actions(state), self.qfunction)

    ###########
    # Learner #
    ###########

    def episode(self):
        while not self.env.is_terminal():
            state = self.env.cur_state()
            action = self.policy.action(state)
            reward, next_state = self.env.do_action(action)
            if self.experience_replay:
                self.memory.append((state, action, reward, next_state))
                state, _, reward, next_state = random.choice(self.memory)
            best_qvalue = self.best_qvalue(next_state)
            update = reward + (self.discount_factor * best_qvalue)
            self.qfunction.update(state, update)
