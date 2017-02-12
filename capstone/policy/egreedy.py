import random
from . import Policy
from . import GreedyPolicy
from . import RandomPolicy


class EGreedyPolicy(Policy):

    def __init__(self, e):
        self.e = e
        self.greedy = GreedyPolicy()
        self.rand = RandomPolicy()

    def action(self, vf, state, actions=None):
        policy = self.rand if random.random() < self.e else self.greedy
        return policy.action(vf, state, actions)
