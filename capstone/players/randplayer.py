import random
from .. import Player


class RandPlayer(Player):

    name = 'Random Player'

    def __str__(self):
        return 'Random Player'

    ##########
    # Player #
    ##########

    def choose_move(self, game):
        return random.choice(game.legal_moves())
