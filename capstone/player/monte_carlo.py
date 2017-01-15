import random
from collections import defaultdict, Counter
from . import Player
from ..util import utility


class MonteCarlo(Player):

    name = 'MonteCarlo'

    def __init__(self, n_sims=100):
        self.n_sims = n_sims
    
    def __repr__(self):
        return type(self).name

    def __str__(self):
        return type(self).name

    def move(self, game):
        counter = defaultdict(int)
        for i in range(self.n_sims):
            for move in game.legal_moves():
                new_game = game.copy()
                new_game.make_move(move)
                while not new_game.is_over():
                    rand_move = random.choice(new_game.legal_moves())
                    new_game.make_move(rand_move)
                counter[move] += utility(new_game, game.cur_player())
        m = Counter(counter).most_common(1)
        return m[0][0]

    ##########
    # Player #
    ##########

    def choose_move(self, game):
        return self.move(game)
