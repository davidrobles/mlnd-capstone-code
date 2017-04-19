# -*- coding: utf-8 -*-
import numpy as np
from keras.layers import Activation, Conv2D, Dense, Dropout, Flatten, MaxPooling2D
from keras.models import Sequential
from keras.optimizers import SGD
from ..qfunction import QFunction
from ...game.games import Connect4 as C4
from ...game.utils import normalize_board

def normalize_board(board):
    def mapper(t):
        if t == 'X':
            return np.array([1.0])
        elif t == 'O':
            return np.array([-1.0])
        else:
            return np.array([0.0])
    vfunc = np.vectorize(mapper)
    robles = np.array(board)
    x = vfunc(robles)
    x = x.reshape(C4.ROWS, C4.COLS, -1)
    return x


mapping = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6}


class Connect4QNetwork(QFunction):

    '''DQN for Connect 4.'''

    def __init__(self):

        model = Sequential()
        model.add(Conv2D(64, kernel_size=(3, 3), input_shape=(C4.ROWS, C4.COLS, 1)))
        model.add(Activation('relu'))
        model.add(Conv2D(64, kernel_size=(3, 3), padding='same'))
        model.add(Activation('relu'))
        model.add(Conv2D(64, kernel_size=(3, 3), padding='same'))
        model.add(Activation('relu'))
        model.add(Conv2D(64, kernel_size=(3, 3), padding='same'))
        model.add(Activation('relu'))
        model.add(Flatten())
        model.add(Dense(256))
        model.add(Dense(7))
        model.add(Activation('tanh'))

        sgd = SGD(lr=0.001)
        model.compile(loss='mse', optimizer=sgd)
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
            a = mapping[action]
            y[0][a] = updates[i]
            ylist.append(y[0])
        x = np.array(xlist)
        y = np.array(ylist)
        self.model.train_on_batch(x, y)

    #############
    # QFunction #
    #############

    def __getitem__(self, state_action):
        state, action = state_action
        x = normalize_board(state.board)
        value = self.model.predict(np.array([x]), batch_size=1)
        a = mapping[action]
        assert isinstance(a, int)
        return value[0][a]

    def best_value(self, state, actions, max_or_min):
        x = normalize_board(state.board)
        output = self.model.predict(np.array([x]))
        action_values = []
        for action in actions:
            action_idx = mapping[action]
            action_values.append(output[0][action_idx])
        return max_or_min(action_values)
