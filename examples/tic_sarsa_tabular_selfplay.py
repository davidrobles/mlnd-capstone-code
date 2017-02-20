'''
Sarsa is used to learn the state-action values for a
Tic-Tac-Toe board position against a fixed Alpha-Beta opponent
'''
from capstone.game.games import TicTacToe
from capstone.game.players import AlphaBeta
from capstone.game.utils import tic2pdf
from capstone.rl import FixedGameMDP, Environment
from capstone.rl.learners import Sarsa

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
