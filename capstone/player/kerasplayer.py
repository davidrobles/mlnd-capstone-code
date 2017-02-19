from . import Player
from ..utils import norm_tic_board, utility
from keras.models import load_model


class Keras(Player):
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

    def choose_move(self, state):
        assert state.cur_player() == 0
        best_action = None
        best_value = -1000000
        for action in state.legal_moves():
            s = state.copy()
            s = s.make_move(action)
            value = self.model.predict(norm_tic_board(s), batch_size=1)
            assert value >= -1.0 and value <= 1.0
            if value > best_value:
                best_action = action
                best_value = value
        return best_action
