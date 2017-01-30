from capstone.game import TicTacToe
from capstone.player import RandPlayer
from capstone.util import play_series

game = TicTacToe()
players = [RandPlayer(), RandPlayer()]
play_series(game, players)
