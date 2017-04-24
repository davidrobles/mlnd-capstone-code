import numpy as np
from keras.models import load_model
from ..games import Connect4 as C4
from ..player import Player
from ..utils import normalize_board, utility


class KerasPlayer(Player):
    '''
    Takes moves based on a Keras neural network model.
    Assumes that the model predicts the values for a
    board from the point of view of the first player.
    '''

    name = 'Keras'

    def __init__(self, filepath):
        self.model = load_model(filepath)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def _move_values(self, game):
        move_values = []
        for move in game.legal_moves():
            next_game = game.copy().make_move(move)
            input_values = normalize_board(next_game.board)
            value = self.model.predict(input_values, batch_size=1)
            assert value >= -1.0 and value <= 1.0
            move_values.append({'move': move, 'value': value})
        return move_values

    ##########
    # Player #
    ##########

    def choose_move(self, game):
        move_values = self._move_values(game)
        best = max if game.cur_player() == 0 else min
        return best(move_values, key=lambda mv: mv['value'])['move']


def normalize_board(board, player_idx):
    def mapper(t):
        if t == 'X':
            return np.array([1.0 if player_idx == 0 else -1.0])
        elif t == 'O':
            return np.array([-1.0 if player_idx == 0 else 1.0])
        else:
            return np.array([0.0])
    x = np.vectorize(mapper)(np.array(board))
    x = x.reshape(C4.ROWS, C4.COLS, -1)
    return x


class KerasStatePlayer(Player):

    def __init__(self, filepath):
        self.model = load_model(filepath)

    def choose_move(self, game):
        action_values = []
        for move in game.legal_moves():
            next_state = game.copy().make_move(move)
            # if next_state.is_over():
            #     return move
            x = normalize_board(next_state.board, game.cur_player())
            value = self.model.predict(np.array([x]), batch_size=1)
            action_values.append((move, value[0][0]))
        best_move, _ = max(action_values, key=lambda sa: sa[1])
        return best_move


