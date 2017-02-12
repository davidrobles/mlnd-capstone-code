import random
from . import Policy
from . import GreedyPolicy
from . import RandomPolicy


class EGreedyPolicy(Policy):

    def __init__(self, epsilon):
        self.epsilon = epsilon
        self.greedy = GreedyPolicy()
        self.rand = RandomPolicy()

    def action(self, vf, state, actions=None):
        policy = self.rand if random.random() < self.epsilon else self.greedy
        return policy.action(vf, state, actions)
