import numpy as np
from keras.layers import Activation, Conv2D, Dense, Dropout, Flatten, MaxPooling2D
from keras.models import Sequential
from keras.optimizers import SGD
from ..qfunction import QFunction
from ...game.games import Connect4 as C4


def normalize_board(board):
    """
    Takes a board in this format:

        board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', 'O', ' ', 'O', ' '],
                 [' ', ' ', 'O', 'X', ' ', 'X', ' '],
                 [' ', ' ', 'X', 'O', ' ', 'X', ' '],
                 [' ', 'O', 'O', 'X', 'X', 'X', 'O']]

    and returns:

        board = [[[0],  [0],  [0],  [0], [0],  [0],  [0]],
                 [[0],  [0],  [0],  [0], [0],  [0],  [0]],
                 [[0],  [0],  [0], [-1], [0], [-1],  [0]],
                 [[0],  [0], [-1],  [1], [0],  [1],  [0]],
                 [[0],  [0],  [1], [-1], [0],  [1],  [0]],
                 [[0], [-1], [-1],  [1], [1],  [1], [-1]]]
    """

    def mapper(t):
        if t == 'X':
            return np.array([1.0])
        elif t == 'O':
            return np.array([-1.0])
        else:
            return np.array([0.0])
    x = np.vectorize(mapper)(np.array(board))
    x = x.reshape(C4.ROWS, C4.COLS, -1)
    return x


class Connect4DeepNetwork(QFunction):

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
        model.compile(loss='mse', optimizer=SGD(lr=0.001))
        self.model = model

    def minibatch_update(self, experiences):
        xlist = []
        ylist = []
        for _, _, reward, next_state in experiences:
            x = normalize_board(next_state.board)
            if next_state.is_over():
                update = reward
            else:
                output = self.model.predict(np.array([x]))
                update = reward + (0.99 * output[0][0])
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
        next_state = state.copy().make_move(action)
        x = normalize_board(next_state.board)
        value = self.model.predict(np.array([x]), batch_size=1)
        return value[0]
