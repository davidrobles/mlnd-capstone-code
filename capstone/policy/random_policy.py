import random
from . import Policy


class RandomPolicy(Policy):

    def action(self, vf, state, actions=None):
        if not actions:
            raise ValueError('Environment must have at least one available action.')
        return random.choice(actions)
