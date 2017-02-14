import random
from ..util import check_random_state


class ZobristHashing(object):

    def __init__(self, n_positions, n_pieces, random_state=None):
        size = n_positions * n_pieces
        self.table = [random.getrandbits(32) for i in range(size)]
        self.n_positions = n_positions
        self.n_pieces = n_pieces

    def __call__(self, board):
        result = 0
        for i in range(self.n_positions):
            if board[i] != ' ':
                result ^= self.table[i * self.n_pieces + board[i]]
        return result
