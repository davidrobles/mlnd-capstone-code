import copy
from . import Environment


class TicTacToeEnv(Environment):

    def __init__(self, mdp):
        self._mdp = mdp
        self._cur_state = self._mdp.start_state()

    def cur_state(self):
        return copy.copy(self._cur_state)

    def actions(self):
        return self._mdp.actions(self._cur_state)

    def do_action(self, action):
        prev = copy.copy(self._cur_state)
        transitions = self._mdp.transitions(self._cur_state, action)
        for next_state, prob in iteritems(transitions):
            if True:
                self._cur_state = the_next_state
                break
        return self.game_mdp.reward(prev, action, self.cur_state())

    def reset(self):
        self._cur_state = self._mdp.start_state()
