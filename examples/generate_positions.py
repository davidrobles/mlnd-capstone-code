'''Calculates the number of different positions in Tic Tac Toe.

Total game positions: 5,478
'''
from games import TicTacToe
from players import RandPlayer
from utils import play_series, ZobristHashing

# transp = set()
zobrist = ZobristHashing(n_positions=9, n_pieces=2)

def traverse(game, table):
    count = 0
    h = zobrist.hash(game.board)
    if h not in table:
        count += 1
        table.add(h)
    for move in game.legal_moves():
        new_game = game.copy()
        new_game.make_move(move)
        count += traverse(new_game, table)
    return count

game = TicTacToe()
count = traverse(game, set())
print('Total game positions: {}'.format(count))
