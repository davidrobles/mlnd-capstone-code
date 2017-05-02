import numpy as np
from ..player import Player
from ..utils import utility


class AlphaBeta(Player):

    name = 'Alpha-Beta'

    def __init__(self, eval_func=utility, max_depth=np.inf):
        self._eval = eval_func
        self._max_depth = max_depth

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def _ab(self, game, cur_depth, alpha, beta):
        if game.is_over() or cur_depth == self._max_depth:
            return None, self._eval(game, game.cur_player())
        best_move = None
        best_score = -np.inf
        for move in game.legal_moves():
            _, score = self._ab(game=game.copy().make_move(move),
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
        move, _ = self._ab(game, cur_depth=0, alpha=-np.inf, beta=np.inf)
        return move

    def get_action(self, game):
        move, _ = self._ab(game, cur_depth=0, alpha=-np.inf, beta=np.inf)
        return move
