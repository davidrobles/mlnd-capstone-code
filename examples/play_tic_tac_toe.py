from capstone.game import TicTacToe
from capstone.player import RandPlayer
from capstone.utils import play_match

game = TicTacToe()
players = [RandPlayer(), RandPlayer()]
play_match(game, players)
