from capstone.game import TicTacToe
from capstone.player import MonteCarlo, RandPlayer
from capstone.utils import play_series

game = TicTacToe()
players = [MonteCarlo(), RandPlayer()]
n_matches = 10
play_series(game, players, n_matches)
print('')
players.reverse()
play_series(game, players, n_matches)
