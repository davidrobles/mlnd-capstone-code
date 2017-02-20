import random
from collections import defaultdict, Counter
from ..player import Player
from ..utils import utility


class MonteCarlo(Player):

    name = 'MonteCarlo'

    def __init__(self, n_sims=1000):
        self.n_sims = n_sims

    def __repr__(self):
        return type(self).name

    def __str__(self):
        return type(self).name

    ##########
    # Player #
    ##########

    def choose_move(self, game):
        counter = defaultdict(int)
        for i in range(self.n_sims):
            for move in game.legal_moves():
                new_game = game.copy()
                new_game.make_move(move)
                while not new_game.is_over():
                    rand_move = random.choice(new_game.legal_moves())
                    new_game.make_move(rand_move)
                counter[move] += utility(new_game, game.cur_player())
        best_move, count = Counter(counter).most_common(1)[0]
        return best_move
