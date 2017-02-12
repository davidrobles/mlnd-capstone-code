'''
In this example we use Q-learning via self-play to learn
the value function of all Tic-Tac-Toe positions.
'''
from capstone.environment import Environment
from capstone.game import TicTacToe
from capstone.mdp import GameMDP
from capstone.rl import QLearningSelfPlay
from capstone.rl.tabularf import TabularF
from capstone.util import tic2pdf

game = TicTacToe()
env = Environment(GameMDP(game))
qlearning = QLearningSelfPlay(env, n_episodes=1000)
qlearning.learn()

for move in game.legal_moves():
    print('-' * 80)
    value = qlearning.qf[(game, move)]
    new_game = game.copy().make_move(move)
    print(value)
    print(new_game)
