from capstone.game.games import TicTacToe
from capstone.game.players import AlphaBeta, RandPlayer
from capstone.game.utils import play_match

game = TicTacToe()
players = [AlphaBeta(), RandPlayer()]
play_match(game, players)
