import random
from utils import default_util_func


class AlphaBeta(object):

    name = 'Alpha-Beta Pruning'

    def __init__(self, eval_func=default_util_func, max_depth=1000):
        self.eval_func = eval_func
        self.max_depth = max_depth

    def choose_move(self, game):
        return self._ab(game, 0, -100000000, 100000000)[0]

    def _ab(self, game, cur_depth, alpha, beta):
        if game.is_over() or cur_depth == self.max_depth:
            return [-1, self.eval_func(game, game.cur_player)]
        best_move = -1
        best_score = -100000000
        for move in game.legal_moves():
            new_game = game.copy()
            new_game.make_move(move)
            _, cur_score = self._ab(new_game, cur_depth + 1, -beta, -max([alpha, best_score]))
            cur_score = -cur_score
            if cur_score > best_score:
                best_score = cur_score
                best_move = move
                if best_score >= beta:
                    return [best_move, best_score]
        return best_move, best_score
