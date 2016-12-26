from . import Policy


class GreedyPolicy(Policy):

    def action(self, env, vf=None, qf=None):
        state = env.cur_state()
        actions = env.actions()
        if not actions:
            print('called with no actions')
            return 0
        state_actions = [(state, action) for action in actions]
        _, best_action = max(state_actions, key=lambda sa: qf[sa])
        return best_action
