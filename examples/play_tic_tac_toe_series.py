from capstone.game.games import TicTacToe
from capstone.game.players import RandPlayer
from capstone.game.utils import play_series

game = TicTacToe()
players = [RandPlayer(), RandPlayer()]
play_series(game, players)
