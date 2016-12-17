from games import TicTacToe
from players import RandPlayer
from utils import play_series

class ZobristHashing(object):

    def __init__(self):
        self.table = self._init_zobrist()

    def _init_zobrist(self):
        import random
        table = [[] for _ in range(9)]
        for i in range(9):
            for j in range(2):
                table[i].append(random.getrandbits(32))
        return table

    def hash(self, board):
        h = 0
        for i in range(9):
            if board[i] != ' ':
                j = board[i]
                h = h ^ self.table[i][j]
        return h


game = TicTacToe()
count = 0
transp = set()

zobrist = ZobristHashing()

def traverse(game, depth=0):
    global count
    global transp
    h = zobrist.hash(game.board)
    if h not in transp:
        count +=1
        transp.add(h)
    max_depth = depth
    for move in game.legal_moves():
        new_game = game.copy()
        new_game.make_move(move)
        max_depth = max(max_depth, traverse(new_game, depth + 1))
    return max_depth

max_depth = traverse(game)
print('Total game positions: {}'.format(count))
print('Max Depth: {}'.format(max_depth))
