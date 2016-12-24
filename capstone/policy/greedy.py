from . import Policy


# add a parameter to maximise or minimize the value

class GreedyPolicy(Policy):

    def action(self, env, vf=None, qf=None):
        state = env.cur_state()
        actions = env.actions(state)
        return max([qf[(state, action)] for action in actions])
