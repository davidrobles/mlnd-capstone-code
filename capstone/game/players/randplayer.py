import random
from ..player import Player


class RandPlayer(Player):

    name = 'RandPlayer'

    def __str__(self):
        return 'RandPlayer'

    def __repr__(self):
        return 'RandPlayer'

    ##########
    # Player #
    ##########

    def choose_move(self, game):
        return random.choice(game.legal_moves())
