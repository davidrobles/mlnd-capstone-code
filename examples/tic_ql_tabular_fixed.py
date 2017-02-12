'''
Q-Learning is used to learn the state-action values for a
Tic-Tac-Toe board position against a fixed Alpha-Beta opponent.
'''
from capstone.environment import Environment
from capstone.game import TicTacToe
from capstone.mdp import GameMDP
from capstone.player import AlphaBeta
from capstone.rl import QLearning
from capstone.util import tic2pdf

board = [['X', ' ', ' '],
         ['O', 'X', ' '],
         [' ', 'O', ' ']]
game = TicTacToe(board)
env = Environment(GameMDP(game, AlphaBeta(), 1))
qlearning = QLearning(env, n_episodes=1000)
qlearning.learn()
tic2pdf('figures/tic_ql_current.pdf', game.board)

for move in game.legal_moves():
    value = qlearning.qf[(game, move)]
    print('Move: %d' % move)
    print('Value: %f' % value)
    new_game = game.copy().make_move(move)
    print(new_game)
    filename = 'figures/tic_ql_move_%d_value_%.4f.pdf' % (move, value)
    tic2pdf(filename, new_game.board)