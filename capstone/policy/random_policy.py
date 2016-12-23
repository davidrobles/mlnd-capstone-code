import random
from . import Policy


class RandomPolicy(Policy):

    def action(self, env, vf=None, qf=None):
        return random.choice(env.actions(env.cur_state()))
