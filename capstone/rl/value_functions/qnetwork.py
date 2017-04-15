# -*- coding: utf-8 -*-
import numpy as np
from keras.layers import Activation, Conv2D, Dense, Dropout, Flatten, MaxPooling2D
from keras.models import Sequential
from keras.optimizers import SGD
from ..qfunction import QFunction
from ...game.utils import normalize_board


def convert_me(state):
    def mapper(t):
        if t == 'X':
            return np.array([1.0])
        elif t == 'O':
            return np.array([-1.0])
        else:
            return np.array([0.0])
    vfunc = np.vectorize(mapper)
    robles = np.array(state.board)
    x = vfunc(robles)
    x = x.reshape(6, 7, -1)
    return x


class QNetwork(QFunction):
    '''A Q-Network is a neural network function approximator with θ weights.'''

    # def __init__(self, mapping, n_input_units, n_hidden_layers, n_output_units,
    #              n_hidden_units=10, learning_rate=0.01):
    #     self.mapping = mapping
    #     model = Sequential()
    #     model.add(Convolution2D())
    #     # input layer
    #     model.add(Dense(n_hidden_units, input_shape=(n_input_units,)))
    #     model.add(Activation('relu'))
    #     # hidden layers
    #     for _ in xrange(n_hidden_layers):
    #         model.add(Dense(n_hidden_units))
    #         model.add(Activation('relu'))
    #     # output layer
    #     model.add(Dense(n_output_units))
    #     model.add(Activation('tanh'))
    #     model.compile(loss='mse', optimizer=SGD(lr=learning_rate))
    #     self.model = model

    def __init__(self, mapping, n_input_units, n_hidden_layers, n_output_units,
                 n_hidden_units=10, learning_rate=0.01):

        self.mapping = mapping
        s = (6, 7, 1)
        model = Sequential()
        model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=s))
        model.add(Conv2D(64, (3, 3), activation='relu'))

        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))
        model.add(Flatten())
        model.add(Dense(128, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(7))
        model.add(Activation('tanh'))
        model.compile(loss='mse', optimizer='rmsprop')
        self.model = model

    def minibatch_update(self, experiences, updates):
        batch_size = len(experiences)
        assert len(experiences) == len(updates)
        xlist = []
        ylist = []
        for i in range(len(experiences)):
            state, action, reward, next_state = experiences[i]
            # import pdb; pdb.set_trace()
            # x = normalize_board(state.board)
            x = convert_me(state)
            xlist.append(x)
            y = self.model.predict(np.array([x]))
            a = self.mapping[action]
            y[0][a] = updates[i]
            ylist.append(y[0])
        x = np.array(xlist)
        y = np.array(ylist)
        self.model.train_on_batch(x, y)

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
        # x = normalize_board(state.board)
        # x = np.array([x])
        x = convert_me(state)
        value = self.model.predict(np.array([x]), batch_size=1)
        a = self.mapping[action]
        assert isinstance(a, int)
        return value[0][a]

    def best_value(self, state, actions, max_or_min):
        # def mapper(t):
        #     if t == 'X':
        #         return np.array([1.0])
        #     elif t == 'O':
        #         return np.array([-1.0])
        #     else:
        #         return np.array([0.0])
        # vfunc = np.vectorize(mapper)
        # robles = np.array(state.board)
        # x = vfunc(robles)
        # x = x.reshape(6, 7, -1)
        x = convert_me(state)
        # import pdb; pdb.set_trace()
        output = self.model.predict(np.array([x]))
        vals = []
        for aa in actions:
            hey = self.mapping[aa]
            vals.append(output[0][self.mapping[aa]])
        return max_or_min(vals)
