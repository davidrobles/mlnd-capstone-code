from capstone.game import TicTacToe
from capstone.player import MonteCarlo, RandPlayer
from capstone.util import play_series

game = TicTacToe()
players = [MonteCarlo(), RandPlayer()]
n_matches = 10
play_series(game, players, n_matches)
players.reverse()
play_series(game, players, n_matches)
