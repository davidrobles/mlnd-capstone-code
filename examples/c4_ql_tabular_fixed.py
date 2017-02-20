'''
Q-Learning is used to learn the state-action values for a Connect 4 board
position against a fixed Alpha-Beta opponent.
'''
from capstone.game.games import Connect4
from capstone.game.players import AlphaBeta
from capstone.game.utils import c42pdf
from capstone.rl import FixedGameMDP, Environment
from capstone.rl.learners import QLearning

board = [['X', 'O', 'O', ' ', 'O', ' ', ' '],
         ['X', 'O', 'X', ' ', 'X', ' ', ' '],
         ['O', 'X', 'O', 'X', 'O', 'X', 'O'],
         ['O', 'X', 'O', 'X', 'O', 'X', 'O'],
         ['X', 'O', 'X', 'O', 'X', 'O', 'X'],
         ['X', 'O', 'X', 'O', 'X', 'O', 'X']]
game = Connect4(board)
env = Environment(FixedGameMDP(game, AlphaBeta(), 1))
qlearning = QLearning(env, n_episodes=1000)
qlearning.learn()
c42pdf('figures/c4_ql_current.pdf', game.board)

for move in game.legal_moves():
    print('*' * 80)
    value = qlearning.qf[(game, move)]
    print('Move: %s' % move)
    print('Value: %f' % value)
    new_game = game.copy().make_move(move)
    print(new_game)
    filename = 'figures/c4_ql_move_%s_value_%.4f.pdf' % (move, value)
    c42pdf(filename, new_game.board)
