'''
Q-Learning is used to learn the state-action values, Q(s, a) for all
Tic-Tac-Toe board positions against a fixed Alpha-Beta opponent.
'''
from capstone.game.games import TicTacToe
from capstone.game.players import AlphaBeta
from capstone.game.utils import tic2pdf
from capstone.rl import Environment, FixedGameMDP
from capstone.rl.learners import QLearning

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
