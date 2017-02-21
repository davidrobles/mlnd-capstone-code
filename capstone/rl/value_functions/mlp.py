import numpy as np
from keras.layers.core import Dense
from keras.models import Sequential
from keras.optimizers import RMSprop
from ...game.utils import normalize_board


class MLP(object):

    def __init__(self):
        self.model = Sequential()
        self.model.add(Dense(150, input_dim=9, init='lecun_uniform', activation='tanh'))
        self.model.add(Dense(1, init='lecun_uniform', activation='tanh'))
        self.model.compile(loss='mse', optimizer=RMSprop())

    def update(self, state, value):
        x = normalize_board(state.board)
        y = np.array([[value]])
        self.model.fit(x, y, batch_size=1, nb_epoch=1, verbose=0)

    def get_value(self, state):
        value = self.model.predict(normalize_board(state.board), batch_size=1)
        return value[0][0]

    def __getitem__(self, state_action):
        state, action = state_action
        copy = state.copy().make_move(action)
        return self.get_value(copy)
