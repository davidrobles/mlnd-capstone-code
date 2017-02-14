import random
from . import Policy
from . import GreedyPolicy
from . import RandomPolicy
from ..utils import check_random_state


class EGreedy(Policy):

    def __init__(self, e, random_state=None):
        self.e = e
        self.greedy = GreedyPolicy()
        self.rand = RandomPolicy()
        self.random_state = check_random_state(random_state)

    def action(self, vf, state, actions=None):
        policy = self.rand if self.random_state.rand() < self.e else self.greedy
        return policy.action(vf, state, actions)
