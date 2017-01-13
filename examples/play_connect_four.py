from capstone.game import Connect4
from capstone.player import RandPlayer
from capstone.util import play_match

game = Connect4(
    'XO-----'
    'XO-----'
    'OXOXOXO'
    'OXOXOXO'
    'XOXOXOX'
    'XOXOXOX'
)
players = [RandPlayer(), RandPlayer()]
play_match(game, players)
