import random
from . import Policy


class RandomPolicy(Policy):

    def action(self, env, vf=None, qf=None):
        state = env.cur_state()
        actions = env.actions()
        if not actions:
            raise ValueError('Environment must have at least one available action.')
        return random.choice(actions)
