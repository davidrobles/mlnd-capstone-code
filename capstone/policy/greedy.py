from . import Policy


class GreedyPolicy(Policy):

    def action(self, env, vf=None, qf=None):
        state = env.cur_state()
        actions = env.actions()
        if not actions:
            raise ValueError('Environment must have at least one available action.')
        state_actions = [(state, action) for action in actions]
        _, best_action = max(state_actions, key=lambda sa: qf[sa])
        return best_action
