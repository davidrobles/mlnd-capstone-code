from capstone.game.games import Connect4
from capstone.game.players import RandPlayer
from capstone.game.utils import play_series

class MyPlayer(object):

    def choose_move(self, game):
        return game.legal_moves()[0]

my = MyPlayer()

game = Connect4()
players = [my, RandPlayer()]
play_series(game, players, n_matches=1000)
