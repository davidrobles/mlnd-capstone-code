'''
Sarsa is used to learn the state-action values for a
Tic-Tac-Toe board position against a fixed Alpha-Beta opponent
'''
from capstone.environment import Environment
from capstone.game import TicTacToe
from capstone.mdp import FixedGameMDP
from capstone.player import AlphaBeta
from capstone.rl import Sarsa
from capstone.utils import tic2pdf

board = [['X', ' ', ' '],
         ['O', 'X', ' '],
         [' ', 'O', ' ']]
game = TicTacToe(board)
env = Environment(FixedGameMDP(game, AlphaBeta(), 1))
sarsa = Sarsa(env, n_episodes=1000, random_state=0)
sarsa.learn()
tic2pdf('figures/tic_sarsa_current.pdf', game.board)

for move in game.legal_moves():
    print('*' * 80)
    value = sarsa.qf[(game, move)]
    print('Move: %d' % move)
    print('Value: %f' % value)
    new_game = game.copy().make_move(move)
    print(new_game)
    filename = 'figures/tic_sarsa_move_%d_value_%.4f.pdf' % (move, value)
    tic2pdf(filename, new_game.board)
