from capstone.game import TicTacToe
from capstone.player import KerasPlayer, RandPlayer
from capstone.utils import play_series

players = [KerasPlayer('models/qltic.h5'), RandPlayer()]
game = TicTacToe()
play_series(game, players, n_matches=1000)
