from capstone.game.games import TicTacToe
from capstone.game.players import AlphaBeta, RandPlayer
from capstone.game.utils import normalize_board
from capstone.rl import GameMDP, FixedGameMDP, Environment
from capstone.rl.learners import ApproximateQLearning
from capstone.rl.value_functions import MLP

board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]
game = TicTacToe(board)
env = Environment(FixedGameMDP(game, RandPlayer(), 1))
mlp = MLP()
qlearning = ApproximateQLearning(env, qf=mlp, n_episodes=10000, verbose=False)
qlearning.learn()
mlp.model.save('models/qltic.h5')

for move in game.legal_moves():
    print('-' * 80)
    new_game = game.copy().make_move(move)
    value = mlp[game, move]
    print(value)
    print(new_game)
