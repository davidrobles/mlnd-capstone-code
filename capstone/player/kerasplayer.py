from keras.models import load_model
from . import Player
from ..utils import normalize_board, utility


class KerasPlayer(Player):
    '''
    Takes moves based on a Keras neural network model.
    '''

    name = 'Keras'

    def __init__(self, filepath):
        self.model = load_model(filepath)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    ##########
    # Player #
    ##########

    def choose_move(self, game):
        assert game.cur_player() == 0
        best_move = None
        best_value = -1000000
        for move in game.legal_moves():
            next_game = game.copy().make_move(move)
            value = self.model.predict(normalize_board(next_game.board), batch_size=1)
            assert value >= -1.0 and value <= 1.0
            if value > best_value:
                best_move = move
                best_value = value
        return best_move
