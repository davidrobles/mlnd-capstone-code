'''
Q-Learning is used to learn the state-action values for a Connect 4 board
position against a fixed Alpha-Beta opponent.
'''
from capstone.environment import Environment
from capstone.game import Connect4
from capstone.mdp import GameMDP
from capstone.player import AlphaBeta
from capstone.rl import QLearning
from capstone.util import c42pdf

board = [['X', 'O', 'X', 'O', ' ', ' ', ' '],
         ['X', 'O', 'X', 'O', ' ', ' ', ' '],
         ['O', 'X', 'O', 'X', 'O', 'X', 'O'],
         ['O', 'X', 'O', 'X', 'O', 'X', 'O'],
         ['X', 'O', 'X', 'O', 'X', 'O', 'X'],
         ['X', 'O', 'X', 'O', 'X', 'O', 'X']]
game = Connect4(board)
env = Environment(GameMDP(game, AlphaBeta(), 1))
qlearning = QLearning(env, n_episodes=1000)
qlearning.learn()
c42pdf('figures/c4_ql_current.pdf', game.board)

for move in game.legal_moves():
    value = qlearning.qf[(game, move)]
    print('Move: %s' % move)
    print('Value: %f' % value)
    new_game = game.copy().make_move(move)
    print(new_game)
    filename = 'figures/c4_ql_move_%s_value_%.4f.pdf' % (move, value)
    c42pdf(filename, new_game.board)
