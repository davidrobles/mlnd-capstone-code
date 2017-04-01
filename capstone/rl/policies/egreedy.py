from .greedy import Greedy
from .random_policy import RandomPolicy
from ..policy import Policy
from ...utils import check_random_state


class EGreedy(Policy):

    def __init__(self, provider, qf, epsilon=0.1, random_state=None):
        self.provider = provider
        self.qf = qf
        self.epsilon = epsilon
        self.random_state = check_random_state(random_state)
        self.rand = RandomPolicy(provider, self.random_state)
        self.greedy = Greedy(provider, self.qf)

    def action(self, state):
        policy = self.rand if self.random_state.rand() < self.epsilon else self.greedy
        return policy.action(state)
