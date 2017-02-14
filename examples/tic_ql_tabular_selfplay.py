'''
In this example we use Q-learning via self-play to learn
the value function of a Tic-Tac-Toe position.
'''
from capstone.environment import Environment
from capstone.game import TicTacToe
from capstone.mdp import GameMDP
from capstone.rl import QLearningSelfPlay
from capstone.rl.tabularf import TabularF
from capstone.utils import tic2pdf

# generate a board from this position for the report
board = [['X', 'X', ' '],
         ['O', 'O', ' '],
         [' ', ' ', ' ']]
game = TicTacToe(board)
env = Environment(GameMDP(game))
qlearning = QLearningSelfPlay(env, n_episodes=1000, random_state=0)
qlearning.learn()

for move in game.legal_moves():
    print('-' * 80)
    value = qlearning.qf[(game, move)]
    new_game = game.copy().make_move(move)
    print(value)
    print(new_game)
