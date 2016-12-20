from . import MDP
from ..game import TicTacToe
from ..util import default_util_func, ZobristHashing


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

    def actions(self, game):
        return game.legal_moves()

    def is_terminal(self, game):
        return game.is_over()

    def reward(self, game, action, next_game):
        if not next_game.is_over():
            return 0
        return default_util_func(next_game, (self._opp_player_idx + 1) % 2)

    def start_state(self):
        return self._game.copy()

    def states(self):
        if not self._hashed_states:
            def generate_states(game):
                '''Generates all the states for the game'''
                board_hash = self._zobrist_hash(game.board)
                if board_hash not in self._hashed_states:
                    self._hashed_states[board_hash] = game
                for move in game.legal_moves():
                    new_game = game.copy().make_move(move)
                    generate_states(new_game)
            generate_states(self._game)
        return self._hashed_states.values()

    def transitions(self, game, move):
        new_game = game.copy().make_move(move)
        if new_game.cur_player() == self._opp_player_idx:
            chosen_move = self._opp_player.choose_move(new_game)
            new_game.make_move(chosen_move)
        return [(new_game, 1.0)]
