from ..policy import Policy


class Greedy(Policy):

    def __init__(self, provider, qfunction, selfplay=False):
        self.provider = provider
        self.qfunction = qfunction
        self.selfplay = selfplay

    def action(self, state):
        actions = self.provider(state)
        if not actions:
            raise ValueError('Must have at least one available action.')
        if self.selfplay:
            best_func = max if state.cur_player() == 0 else min
        else:
            best_func = max
        state_actions = [(state, action) for action in actions]
        _, best_action = best_func(state_actions, key=lambda sa: self.qfunction[sa])
        return best_action
