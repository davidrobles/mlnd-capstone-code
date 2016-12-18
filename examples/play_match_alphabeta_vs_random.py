from capstone.games import TicTacToe
from capstone.players import AlphaBeta, RandPlayer
from capstone.util import play_match

game = TicTacToe()
players = [AlphaBeta(), RandPlayer()]
play_match(game, players)
