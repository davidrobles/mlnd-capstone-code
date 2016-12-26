from . import Policy


class GreedyPolicy(Policy):

    def action(self, env, vf=None, qf=None):
        if env.is_terminal():
            return 0
        state = env.cur_state()
        actions = env.actions(state)
        return max([qf[(state, action)] for action in actions])
