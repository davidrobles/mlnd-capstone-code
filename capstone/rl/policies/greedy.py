from ..policy import Policy


class Greedy(Policy):

    def __init__(self, action_space, vfunction=None, qfunction=None, selfplay=False):
        if vfunction is None and qfunction is None:
            raise ValueError('Requires either a V-function or Q-function')
        self.action_space = action_space
        self.vfunction = vfunction
        self.qfunction = qfunction
        self.selfplay = selfplay

    def get_action(self, state):
        if state.is_over():
            raise ValueError('No actions available when the game is over.')
        actions = self.action_space(state)
        if not actions:
            raise ValueError('Must have at least one available action.')
        if self.selfplay:
            best_func = max if state.cur_player() == 0 else min
        else:
            best_func = max
        if self.vfunction:
            state_actions = [(state, action) for action in actions]
            _, best_action = best_func(state_actions, key=lambda state: self.vfunction[state])
        else:
            state_actions = [(state, action) for action in actions]
            _, best_action = best_func(state_actions, key=lambda sa: self.qfunction[sa])
        return best_action
