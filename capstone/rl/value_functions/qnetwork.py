# -*- coding: utf-8 -*-
import numpy as np
from keras.layers import Activation, Dense, Dropout
from keras.models import Sequential
from keras.optimizers import Adam, SGD
from ..qfunction import QFunction
from ...game.utils import normalize_board




dropoutRate = 0
dropoutRateInput = 0
# mapping = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6}
mapping = { int(x): int(x) - 1 for x in range(1, 10)}


class QNetwork(QFunction):
    '''A Q-Network is a neural network function approximator with θ weights.'''

    def __init__(self, n_input_units, n_hidden_layers, n_output_units, n_hidden_units=10):
        model = Sequential()
        # input layer
        model.add(Dense(n_hidden_units, input_shape=(n_input_units,)))
        model.add(Activation('relu'))
        model.add(Dropout(dropoutRateInput))
        # hidden layers
        for _ in xrange(n_hidden_layers):
            model.add(Dense(n_hidden_units))
            model.add(Activation('relu'))
            model.add(Dropout(dropoutRate))
        # output layer
        model.add(Dense(n_output_units))
        model.add(Activation('linear'))
        sgd = SGD(lr=0.01)
        model.compile(loss='mse', optimizer=sgd)
        self.model = model
        self.count = 0

    def minibatch(self, experiences, updates):
        assert len(experiences) == len(updates)
        xlist = []
        ylist = []
        for i in range(len(experiences)):
            state, action, reward, next_state = experiences[i]
            x = normalize_board(state.board)
            xlist.append(x)
            y = self.model.predict(np.array([x]))
            a = mapping[action]
            y[0][a] = updates[i]
            ylist.append(y[0])

        x = np.array(xlist)
        y = np.array(ylist)

        # self.model.train_on_batch(x, y)
        self.model.fit(x, y, batch_size=32, verbose=0)
        # print(self.count)
        # self.count += 1

    def update(self, state, action, value):
        x = normalize_board(state.board)
        # y = self.model.predict(x, batch_size=1)
        y = self.model.predict(x)
        # import pdb; pdb.set_trace()
        a = mapping[action]
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
        a = mapping[action]
        assert isinstance(a, int)
        return value[0][a]
