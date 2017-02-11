'''
In this example we use Q-learning via self-play to learn
the value function of a Tic-Tac-Toe position.
'''
from capstone.environment import Environment
from capstone.game import TicTacToe
from capstone.mdp import RealGameMDP
from capstone.rl import QLearningSelfPlay
from capstone.util import tic2pdf

# generate a board from this position for the report
board = [['X', 'X', ' '],
         ['O', 'O', ' '],
         [' ', ' ', ' ']]
game = TicTacToe(board)
env = Environment(RealGameMDP(game))
qf = {}
QLearningSelfPlay(env, qf=qf, n_episodes=1000).learn()

for move in game.legal_moves():
    print('-' * 80)
    value = qf[(game, move)]
    new_game = game.copy().make_move(move)
    print(value)
    print(new_game)
