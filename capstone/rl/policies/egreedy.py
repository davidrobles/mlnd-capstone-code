from .greedy import Greedy
from .random_policy import RandomPolicy
from ..policy import Policy
from ...utils import check_random_state


class EGreedy(Policy):

    def __init__(self, provider, e, random_state=None):
        self.provider = provider
        self.e = e
        self.random_state = check_random_state(random_state)
        self.rand = RandomPolicy(provider, self.random_state)
        self.greedy = Greedy(provider)

    def action(self, state):
        policy = self.rand if self.random_state.rand() < self.e else self.greedy
        return policy.action(state)
