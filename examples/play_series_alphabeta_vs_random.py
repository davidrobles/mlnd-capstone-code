from capstone.games import TicTacToe
from capstone.players import AlphaBeta, RandPlayer
from capstone.utils import play_series

game = TicTacToe()
players = [AlphaBeta(), RandPlayer()]
n_matches=10
play_series(game, players, n_matches)
