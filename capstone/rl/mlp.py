from keras.layers.core import Dense
from keras.models import Sequential
from keras.optimizers import RMSprop


class MLP(object):

    def __init__(self):
        self.model = Sequential()
        self.model.add(Dense(150, input_dim=9, init='lecun_uniform', activation='tanh'))
        self.model.add(Dense(1, init='lecun_uniform', activation='tanh'))
        self.model.compile(loss='mse', optimizer=RMSprop())
