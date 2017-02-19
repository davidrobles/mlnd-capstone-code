from ..policy import Policy


class Greedy(Policy):

    def action(self, state, actions=None, vf=None):
        if not actions:
            raise ValueError('Environment must have at least one available action.')
        state_actions = [(state, action) for action in actions]
        _, best_action = max(state_actions, key=lambda sa: vf[sa])
        return best_action
