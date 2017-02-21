'''
In this example we use Q-learning via self-play to learn
the value function of a Tic-Tac-Toe position.
'''
from capstone.game.games import TicTacToe
from capstone.game.utils import tic2pdf
from capstone.rl import Environment, GameMDP
from capstone.rl.learners import QLearningSelfPlay

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
    value = qlearning.qf[game, move]
    new_game = game.copy().make_move(move)
    print(value)
    print(new_game)
