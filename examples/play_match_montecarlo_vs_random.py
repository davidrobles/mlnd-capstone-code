from capstone.game import TicTacToe
from capstone.player import MonteCarlo, RandPlayer
from capstone.util import play_match

game = TicTacToe()
players = [MonteCarlo(), RandPlayer()]
play_match(game, players)
