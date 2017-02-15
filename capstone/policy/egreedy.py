import random
from .greedy import Greedy
from .policy import Policy
from .random_policy import RandomPolicy
from ..utils import check_random_state


class EGreedy(Policy):

    def __init__(self, e, random_state=None):
        self.e = e
        self.greedy = Greedy()
        self.rand = RandomPolicy()
        self.random_state = check_random_state(random_state)

    def action(self, state, actions=None, vf=None):
        policy = self.rand if self.random_state.rand() < self.e else self.greedy
        return policy.action(vf, state, actions)
