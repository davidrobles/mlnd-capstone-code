from capstone.games import TicTacToe
from capstone.players import RandPlayer
from capstone.util import play_match

game = TicTacToe()
players = [RandPlayer(), RandPlayer()]
play_match(game, players)
