from . import MDP
from ..utils import utility


class GameMDP(MDP):
    '''
    A Markov Decision Process for a Game. Converts a game into an MPD by
    making an opponent with fixed behavior part of the environment.
    '''

    def __init__(self, game):
        self._game = game
        self._states = {}

    def actions(self, state):
        return [None] if state.is_over() else state.legal_moves()

    def is_terminal(self, state):
        return state.is_over()

    def reward(self, state, action, next_state):
        # return the utility from the point of view of the first player
        return utility(next_state, 0) if next_state.is_over() else 0

    def start_state(self):
        return self._game.copy()

    def states(self):
        if not self._states:
            def generate_states(game):
                '''Generates all the states for the game'''
                if game not in self._states:
                    self._states[game] = game
                for move in game.legal_moves():
                    new_game = game.copy().make_move(move)
                    generate_states(new_game)
            generate_states(self._game)
        return self._states

    def transitions(self, state, action):
        if state.is_over():
            return [(state, 1.0)]
        new_game = state.copy().make_move(action)
        return [(new_game, 1.0)]
