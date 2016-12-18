from capstone.games import TicTacToe
from capstone.players import RandPlayer
from capstone.utils import play_series

game = TicTacToe()
players = [RandPlayer(), RandPlayer()]
play_series(game, players)
