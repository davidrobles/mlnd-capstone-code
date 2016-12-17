from games import TicTacToe
from players import RandPlayer
from utils import play_series, ZobristHashing


game = TicTacToe()
count = 0
transp = set()
n_positions = 9
n_pieces = 2
zobrist = ZobristHashing(9, 2)


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
