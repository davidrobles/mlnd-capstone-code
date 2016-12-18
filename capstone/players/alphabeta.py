import random
from . import Player
from utils import default_util_func


class AlphaBeta(Player):

    name = 'Alpha-Beta Pruning'

    def __init__(self, eval_func=default_util_func, max_depth=1000):
        self.eval_func = eval_func
        self.max_depth = max_depth

    def _ab(self, game, cur_depth, alpha, beta):
        if game.is_over() or cur_depth == self.max_depth:
            return None, self.eval_func(game, game.cur_player)
        best_move = -1
        best_score = -100000000
        for move in game.legal_moves():
            new_game = game.copy()
            new_game.make_move(move)
            new_depth = cur_depth + 1
            new_alpha = -beta
            new_beta = -max([alpha, best_score])
            _, score = self._ab(new_game, new_depth, new_alpha, new_beta)
            score = -score
            if score > best_score:
                best_score = score
                best_move = move
                if best_score >= beta:
                    return [best_move, best_score]
        return best_move, best_score

    ##########
    # Player #
    ##########

    def choose_move(self, game):
        return self._ab(game, 0, -100000000, 100000000)[0]
