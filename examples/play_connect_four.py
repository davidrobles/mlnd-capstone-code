from capstone.game import Connect4
from capstone.player import RandPlayer
from capstone.util import play_match

game = Connect4()
players = [RandPlayer(), RandPlayer()]
play_match(game, players)
# print(game)
# game.make_move(0)
# print(game)
# game.make_move(0)
# print(game)
