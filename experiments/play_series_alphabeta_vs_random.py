from capstone.game.games import TicTacToe
from capstone.game.players import AlphaBeta, RandPlayer
from capstone.game.utils import play_series

game = TicTacToe()
players = [AlphaBeta(), RandPlayer()]
print('Players: {}\n'.format(players))
n_matches = 10
play_series(game, players, n_matches)
players.reverse()
print('\nPlayers: {}\n'.format(players))
play_series(game, players, n_matches)
