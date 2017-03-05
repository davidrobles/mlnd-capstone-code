import numpy as np
from keras.layers import Activation, Dense, Dropout
from keras.models import Sequential
from keras.optimizers import Adam
from ..qfunction import QFunction
from ...game.utils import normalize_board


dropoutRate = 0
dropoutRateInput = 0


class DQN(QFunction):
    '''Deep Q-Network'''

    def __init__(self, n_hidden_units=410, n_hidden_layers=3):
        model = Sequential()
        # input layer
        model.add(Dense(n_hidden_units, input_shape=(42,), init='uniform'))
        model.add(Activation('relu'))
        model.add(Dropout(dropoutRateInput))
        # hidden layers
        for _ in xrange(n_hidden_layers):
            model.add(Dense(n_hidden_units, init='uniform'))
            model.add(Activation('relu'))
            model.add(Dropout(dropoutRate))
        # output layer
        model.add(Dense(1, init='uniform'))
        model.add(Activation('tanh'))
        model.compile(loss='mse', optimizer='adam')
        self.model = model

    def update(self, state, value):
        x = normalize_board(state.board)
        y = np.array([[value]])
        self.model.fit(x, y, batch_size=1, nb_epoch=1, verbose=0)

    #############
    # QFunction #
    #############

    def __getitem__(self, state_action):
        state, action = state_action
        copy = state.copy().make_move(action)
        value = self.model.predict(normalize_board(copy.board), batch_size=1)
        return value[0][0]
