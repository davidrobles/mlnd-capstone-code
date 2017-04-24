from capstone.game.games import TicTacToe
from capstone.game.players import MonteCarlo, RandPlayer
from capstone.game.utils import play_match

game = TicTacToe()
players = [MonteCarlo(), RandPlayer()]
play_match(game, players)
