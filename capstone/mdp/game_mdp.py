from copy import copy
from . import MDP
from ..game import TicTacToe
from ..util import ZobristHashing


class GameMDP(MDP):
    '''
    A Markov Decision Process for a Game. Converts a game into an MPD by
    using a deterministic player as an opponent.
    '''

    def __init__(self, game, opp_player, opp_player_idx):
        '''
        opp_player: the opponent player
        opp_player_idx: the player idx position of the opponent player in
                        the game
        '''
        self._game = game
        self._opp_player = opp_player
        self._opp_player_idx = opp_player_idx
        self._hashed_states = {}
        self._zobrist_hash = ZobristHashing(game.n_positions, game.n_pieces)

    def __str__(self):
        return '<MDP states={}>'.format(len(self.states))

    #######
    # MDP #
    #######

    def start_state(self):
        return copy(self._game)

    def states(self):
        if not self._hashed_states:
            def generate_states(game):
                '''Generates all the states for the game'''
                board_hash = self._zobrist_hash(game.board)
                if board_hash not in self._hashed_states:
                    self._hashed_states[board_hash] = game
                for move in game.legal_moves():
                    new_game = copy(game).make_move(move)
                    generate_states(new_game)
            generate_states(self._game)
        return self._hashed_states.values()

    def transitions(self, game, move):
        chosen_move = self._opp_player.choose_move(game)
        if chosen_move != move:
            return {}
        new_game = copy(game)
        new_game.make_move(move)
        hashed = _zobrist_hash(new_game.board)
        return {hashed: 1.0}

    def actions(self, game):
        return game.legal_moves()

    def reward(self, state, action, next_state):
        from ..util import default_util_func
        if not next_state.is_over():
            return 0
        return default_util_func(next_state, (self._opp_player_idx + 1) % 2)

    def is_terminal(self, state):
        return state.is_over()
