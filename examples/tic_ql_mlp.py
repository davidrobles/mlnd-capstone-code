from capstone.game.games import TicTacToe
from capstone.game.players import AlphaBeta, RandPlayer
from capstone.game.utils import normalize_board
from capstone.rl import GameMDP, FixedGameMDP, Environment
from capstone.rl.learners import QLearningKeras
from capstone.rl.value_functions import MLP

board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]
game = TicTacToe(board)
mdp = GameMDP(game)
env = Environment(FixedGameMDP(game, RandPlayer(), 1))
mlp = MLP()
qlearning = QLearningKeras(env, qf=mlp, n_episodes=10000, verbose=False)
qlearning.learn()
mlp.model.save('models/qltic.h5')

for move in game.legal_moves():
    print('-' * 80)
    new_game = game.copy().make_move(move)
    v = normalize_board(new_game.board)
    value = mlp.model.predict(v, batch_size=1)
    print(value[0][0])
    print(new_game)
