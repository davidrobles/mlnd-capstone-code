# -*- coding: utf-8 -*-
import numpy as np
from keras.layers import Activation, Dense
from keras.models import Sequential
from keras.optimizers import SGD
from ..qfunction import QFunction
from ...game.utils import normalize_board


class QNetwork(QFunction):
    '''A Q-Network is a neural network function approximator with θ weights.'''

    def __init__(self, mapping, n_input_units, n_hidden_layers, n_output_units,
                 n_hidden_units=10, learning_rate=0.01):
        self.mapping = mapping
        model = Sequential()
        # input layer
        model.add(Dense(n_hidden_units, input_shape=(n_input_units,)))
        model.add(Activation('relu'))
        # hidden layers
        for _ in xrange(n_hidden_layers):
            model.add(Dense(n_hidden_units))
            model.add(Activation('relu'))
        # output layer
        model.add(Dense(n_output_units))
        model.compile(loss='mse', optimizer=SGD(lr=learning_rate))
        self.model = model

    def minibatch_update(self, experiences, updates):
        batch_size = len(experiences)
        assert len(experiences) == len(updates)
        xlist = []
        ylist = []
        for i in range(len(experiences)):
            state, action, reward, next_state = experiences[i]
            x = normalize_board(state.board)
            xlist.append(x)
            y = self.model.predict(np.array([x]))
            a = self.mapping[action]
            y[0][a] = updates[i]
            ylist.append(y[0])
        x = np.array(xlist)
        y = np.array(ylist)
        self.model.fit(x, y, batch_size=batch_size, verbose=0)

    def update(self, state, action, value):
        x = normalize_board(state.board)
        y = self.model.predict(x)
        a = self.mapping[action]
        y[0][a] = value
        self.model.fit(x, y, batch_size=1, nb_epoch=1, verbose=0)

    #############
    # QFunction #
    #############

    def __getitem__(self, state_action):
        state, action = state_action
        x = normalize_board(state.board)
        x = np.array([x])
        value = self.model.predict(x, batch_size=1)
        a = self.mapping[action]
        assert isinstance(a, int)
        return value[0][a]

    def best_value(self, state, actions, max_or_min):
        board = normalize_board(state.board)
        x = np.array([board])
        output = self.model.predict(x, batch_size=1)
        vals = []
        for aa in actions:
            hey = self.mapping[aa]
            vals.append(output[0][self.mapping[aa]])
        return max_or_min(vals)
