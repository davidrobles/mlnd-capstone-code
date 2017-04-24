from capstone.game.games import TicTacToe
from capstone.game.players import MonteCarlo, RandPlayer
from capstone.game.utils import play_series

game = TicTacToe()
players = [MonteCarlo(), RandPlayer()]
n_matches = 10
play_series(game, players, n_matches)
print('')
players.reverse()
play_series(game, players, n_matches)
