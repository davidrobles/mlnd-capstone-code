from capstone.game import TicTacToe
from capstone.player import AlphaBeta, RandPlayer
from capstone.utils import play_match

game = TicTacToe()
players = [AlphaBeta(), RandPlayer()]
play_match(game, players)
