import random
from . import Policy
from . import GreedyPolicy
from . import RandomPolicy


class EGreedyPolicy(Policy):

    def __init__(self, epsilon):
        self.epsilon = epsilon
        self.greedy_policy = GreedyPolicy()
        self.rand_policy = RandomPolicy()

    def action(self, env, vf=None, qf=None):
        state = env.cur_state()
        actions = env.actions()
        if random.random() < self.epsilon:
            return self.rand_policy.action(env)
        return self.greedy_policy.action(env)
