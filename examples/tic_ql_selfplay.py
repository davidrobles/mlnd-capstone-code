'''
Q-Learning is used to learn the state-action values for a Tic-Tac-Toe board
position against a deterministic Alpha-Beta player.
'''
from capstone.algorithms import QLearning
from capstone.environment import Environment
from capstone.game import TicTacToe
from capstone.mdp import GameMDP
from capstone.player import AlphaBeta
from capstone.util import tic2pdf

board = [['X', ' ', ' '],
         ['O', 'X', ' '],
         [' ', 'O', ' ']]

tic = TicTacToe(board)
dd = {'X': 1.0, ' ': 0.0, 'O': -1.0}

class Hello(object):

    def __getitem__(self, key):
        return

    def __setitem__(self, key, value):
        state, value = key
        print(state)
        pp = state.copy()
        pp.make_move(value)
        hey = [dd[col] for row in pp.board for col in row]
        return

hello = Hello()
hello[(tic, 2)] = 12
