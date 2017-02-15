from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import sgd

from capstone.environment import Environment
from capstone.game import TicTacToe
from capstone.mdp import FixedGameMDP
from capstone.player import AlphaBeta
from capstone.rl import QLearning
from capstone.utils import tic2pdf

class MLP(object):

    def __getitem__(self, key):
        return

    def __setitem__(self, key, value):
        dd = {'X': 1.0, ' ': 0.0, 'O': -1.0}
        state, value = key
        print(state)
        pp = state.copy()
        pp.make_move(value)
        hey = [dd[col] for row in pp.board for col in row]
        return

board = [['X', ' ', ' '],
         ['O', 'X', ' '],
         [' ', 'O', ' ']]
game = TicTacToe(board)
env = Environment(FixedGameMDP(game, AlphaBeta(), 1))
# qlearning = QLearning(env, qf=MLP(), n_episodes=1000)
# qlearning.learn()


hello = MLP()
hello[(game, 2)] = 12
import numpy as np
hidden_size = 50
model = Sequential()
# model.add(Dense(hidden_size, input_shape=(42,), activation='relu'))
# model.add(Dense(hidden_size, activation='relu'))
# model.add(Dense(1))
model.add(Dense(1, input_dim=2))
# model.add(Dense(1, input_shape=(1,)))
model.compile(sgd(lr=.2), "mse")
# print model.predict(np.array([1]))
print(model.summary())
