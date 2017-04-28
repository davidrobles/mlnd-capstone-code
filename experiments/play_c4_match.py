from capstone.game.games import Connect4
from capstone.game.players import RandPlayer
from capstone.game.utils import play_match

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
