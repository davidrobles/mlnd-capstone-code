from games import TicTacToe
from players import AlphaBeta, RandPlayer
from utils import play_match

game = TicTacToe()
players = [AlphaBeta(), RandPlayer()]
play_match(game, players)
