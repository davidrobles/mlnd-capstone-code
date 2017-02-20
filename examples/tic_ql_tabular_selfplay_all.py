'''
In this example the Q-learning algorithm is used via self-play
to learn the state-action values for all Tic-Tac-Toe positions.
'''
from capstone.game.games import TicTacToe
from capstone.game.utils import tic2pdf
from capstone.rl import Environment, GameMDP
from capstone.rl.learners import QLearningSelfPlay
from capstone.rl.value_functions import TabularF

game = TicTacToe()
env = Environment(GameMDP(game))
qlearning = QLearningSelfPlay(env, n_episodes=1000, random_state=0)
qlearning.learn()

for move in game.legal_moves():
    print('-' * 80)
    value = qlearning.qf[(game, move)]
    new_game = game.copy().make_move(move)
    print(value)
    print(new_game)
