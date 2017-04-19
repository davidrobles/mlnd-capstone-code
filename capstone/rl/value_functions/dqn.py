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
        model.add(Dense(1))
        model.add(Activation('tanh'))

        sgd = SGD(lr=0.001)
        model.compile(loss='mse', optimizer=sgd)
        self.model = model

    def minibatch_update(self, experiences):
        xlist = []
        ylist = []
        for state, action, reward, next_state in experiences:
            if next_state.is_over():
                update = reward
            else:
                # best_qvalue = self.best_value(next_state, next_state.legal_moves(), max)
                # best_qvalue = slef.model

                x = normalize_board(next_state.board)
                output = self.model.predict(np.array([x]))
                update = reward + (0.99 * output[0][0])
                # update = reward + (0.99 * best_qvalue)
            x = normalize_board(next_state.board)
            y = np.array([update])
            xlist.append(x)
            ylist.append(y)
        x = np.array(xlist)
        y = np.array(ylist)
        self.model.train_on_batch(x, y)

    #############
    # QFunction #
    #############

    def __getitem__(self, state_action):
        state, action = state_action
        copy = state.copy().make_move(action)
        x = normalize_board(copy.board)
        value = self.model.predict(np.array([x]), batch_size=1)
        return value[0]

    def best_value(self, state, actions, max_or_min):
        action_values = []
        for action in actions:
            copy = state.copy().make_move(action)
            x = normalize_board(copy.board)
            output = self.model.predict(np.array([x]))
            action_values.append(output[0][0])
        return max_or_min(action_values)
