from . import MDP
from ..util import utility


class RealGameMDP(MDP):
    '''
    A Markov Decision Process for a Game. Converts a game into an MPD by
    making an opponent with fixed behavior part of the environment.
    '''

    def __init__(self, game):
        self._game = game
        self._states = {}

    def __str__(self):
        return '<MDP states={}>'.format(len(self.states))

    #######
    # MDP #
    #######

    def actions(self, game):
        return game.legal_moves()

    def is_terminal(self, game):
        return game.is_over()

    def reward(self, game, move, next_game):
        # return the utility from the point of view of the first player
        return utility(next_game, 0) if next_game.is_over() else 0

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

    def transitions(self, game, move):
        if game.is_over():
            return []
        new_game = game.copy().make_move(move)
        return [(new_game, 1.0)]
