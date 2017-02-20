from ..policy import Policy


class Greedy(Policy):

    def action(self, state, actions, qf):
        if not actions:
            raise ValueError('Must have at least one available action.')
        state_actions = [(state, action) for action in actions]
        _, best_action = max(state_actions, key=lambda sa: qf[sa])
        return best_action
