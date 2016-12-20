from capstone.game import TicTacToe
from capstone.player import AlphaBeta, RandPlayer
from capstone.util import play_series

game = TicTacToe()
players = [AlphaBeta(), RandPlayer()]
print('Players: {}\n'.format(players))
n_matches=10
play_series(game, players, n_matches)
players.reverse()
print('\nPlayers: {}\n'.format(players))
play_series(game, players, n_matches)
