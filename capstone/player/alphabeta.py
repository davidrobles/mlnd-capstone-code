from copy import copy
import random
from . import Player
from ..util import default_util_func


class AlphaBeta(Player):

    name = 'Alpha-Beta Pruning'

    def __init__(self, eval_func=default_util_func, max_depth=1000):
        self.eval_func = eval_func
        self.max_depth = max_depth

    def _ab(self, game, cur_depth, alpha, beta):
        if game.is_over() or cur_depth == self.max_depth:
            return None, self.eval_func(game, game.cur_player())
        best_move = None
        best_score = -100000000
        for move in game.legal_moves():
            _, score = self._ab(game=copy(game).make_move(move),
                                cur_depth=cur_depth + 1,
                                alpha=-beta,
                                beta=-max(alpha, best_score))
            score = -score
            if score > best_score:
                best_score = score
                best_move = move
                if best_score >= beta:
                    return best_move, best_score
        return best_move, best_score

    ##########
    # Player #
    ##########

    def choose_move(self, game):
        move, _ = self._ab(game, cur_depth=0, alpha=-100000000, beta=100000000)
        return move
