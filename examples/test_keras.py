from capstone.game.games import TicTacToe
from capstone.game.players import KerasPlayer, RandPlayer
from capstone.game.utils import play_series

players = [KerasPlayer('models/qltic.h5'), RandPlayer()]
game = TicTacToe()
play_series(game, players, n_matches=1000)
