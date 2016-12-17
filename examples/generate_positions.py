'''Calculates the number of different positions in Tic Tac Toe.

Total game positions: 5,478
'''
from games import TicTacToe
from players import RandPlayer
from utils import play_series, ZobristHashing

zobrist = ZobristHashing(n_positions=9, n_pieces=2)

def count_positions(game, table):
    count = 0
    h = zobrist.hash(game.board)
    if h not in table:
        count += 1
        table.add(h)
    for move in game.legal_moves():
        new_game = game.copy()
        new_game.make_move(move)
        count += count_positions(new_game, table)
    return count

game = TicTacToe()
count = count_positions(game, set())
print('Total game positions: {}'.format(count))
