'''
Q-Learning is used to learn the state-action values for a Tic-Tac-Toe board position against a
deterministic Alpha-Beta player.
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
game = TicTacToe(board)
ab = AlphaBeta()
mdp = GameMDP(game, ab, 1)
env = Environment(mdp)
qf = {}
QLearning(env, qf=qf, n_episodes=1000).learn()
tic2pdf(game.board, 'figures/tic_ql_current.pdf')

for move in game.legal_moves():
    value = qf[(game, move)]
    print('Move: %s' % move)
    print('Value: %s' % value)
    new_game = game.copy().make_move(move)
    print(new_game)
    tic2pdf(new_game.board, 'figures/tic_ql_move_%s_value_%.4f.pdf' % (move, value))
