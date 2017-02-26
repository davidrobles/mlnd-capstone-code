from ..player import Player
from ...utils import check_random_state


class RandPlayer(Player):

    name = 'RandPlayer'

    def __init__(self, random_state=None):
        self.random_state = check_random_state(random_state)

    def __str__(self):
        return 'RandPlayer'

    def __repr__(self):
        return 'RandPlayer'

    ##########
    # Player #
    ##########

    def choose_move(self, game):
        return self.random_state.choice(game.legal_moves())
