from ..policy import Policy
from ...utils import check_random_state


class RandomPolicy(Policy):

    def __init__(self, action_space, random_state=None):
        self.action_space = action_space
        self.random_state = check_random_state(random_state)

    def action(self, state):
        actions = self.action_space(state)
        if not actions:
            raise ValueError('Must have at least one available action.')
        return self.random_state.choice(actions)
