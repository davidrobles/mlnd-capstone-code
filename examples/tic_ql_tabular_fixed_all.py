'''
Q-Learning is used to learn the state-action values, Q(s, a) for all
Tic-Tac-Toe board positions against a fixed Alpha-Beta opponent.
'''
from capstone.environment import Environment
from capstone.game import TicTacToe
from capstone.mdp import FixedGameMDP
from capstone.player import AlphaBeta
from capstone.rl import QLearning
from capstone.utils import tic2pdf

game = TicTacToe()
mdp = FixedGameMDP(game, AlphaBeta(), 1)
env = Environment(mdp)
qlearning = QLearning(env, n_episodes=1000)
qlearning.learn()
tic2pdf('figures/tic_ql_tabular_fixed_all_current.pdf', game.board)

for move in game.legal_moves():
    print('*' * 100)
    value = qlearning.qf[(game, move)]
    print('Move: %d' % move)
    print('Value: %f' % value)
    new_game = game.copy().make_move(move)
    print(new_game)
    filename = 'figures/tic_ql_tabular_fixed_all_move_%d_value_%.4f.pdf' % (move, value)
    tic2pdf(filename, new_game.board)
