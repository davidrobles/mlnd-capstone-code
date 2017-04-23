from .greedy import Greedy
from .random_policy import RandomPolicy
from ..policy import Policy
from ...utils import check_random_state


class EGreedy(Policy):

    def __init__(self, action_space, vfunction=None, qfunction=None,
                 epsilon=0.1, selfplay=False, random_state=None):
        if vfunction is None and qfunction is None:
            raise ValueError('Requires either a V-function or Q-function')
        self._action_space = action_space
        self.qfunction = qfunction
        self.vfunction = vfunction
        self.epsilon = epsilon
        self.random_state = check_random_state(random_state)
        self.rand = RandomPolicy(action_space, self.random_state)
        self.greedy = Greedy(action_space, qfunction=self.qfunction,
                             vfunction=self.vfunction, selfplay=selfplay)

    @property
    def action_space(self):
        return self._action_space

    @action_space.setter
    def action_space(self, action_space):
        self._action_space = action_space
        self.rand.action_space = action_space
        self.greedy.action_space = action_space

    ##########
    # Policy #
    ##########

    def action(self, state):
        policy = self.rand if self.random_state.rand() < self.epsilon else self.greedy
        return policy.action(state)
