import numpy as np
from keras.layers.core import Dense
from keras.models import Sequential
from keras.optimizers import RMSprop
from ..qfunction import QFunction
from ...game.utils import normalize_board


class MLP(QFunction):

    def __init__(self):
        self.model = Sequential()
        self.model.add(Dense(150, input_dim=42, init='lecun_uniform', activation='tanh'))
        self.model.add(Dense(1, init='lecun_uniform', activation='tanh'))
        self.model.compile(loss='mse', optimizer=RMSprop())

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
        x = normalize_board(copy.board)
        value = self.model.predict(np.array([x]), batch_size=1)
        return value[0][0]
