from capstone.game.games import TicTacToe
from capstone.game.players import RandPlayer
from capstone.game.utils import play_match

game = TicTacToe()
players = [RandPlayer(), RandPlayer()]
play_match(game, players)
