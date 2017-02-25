'''
The Q-learning algorithm is used to learn the state-action values for all
Tic-Tac-Toe positions by playing games against itself (self-play).
'''
from capstone.game.games import TicTacToe
from capstone.game.players import GreedyQ, RandPlayer
from capstone.game.utils import play_series, tic2pdf
from capstone.rl import Environment, GameMDP
from capstone.rl.learners import QLearningSelfPlay

game = TicTacToe()
env = Environment(GameMDP(game))
qlearning = QLearningSelfPlay(env, n_episodes=10000, verbose=0)
qlearning.learn()

for move in game.legal_moves():
    print('-' * 80)
    value = qlearning.qf[game, move]
    new_game = game.copy().make_move(move)
    print(value)
    print(new_game)

players = [GreedyQ(qlearning.qf), RandPlayer()]
play_series(TicTacToe(), players, n_matches=10000)

# show number of unvisited state?
