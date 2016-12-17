'''Calculates the number of different positions in Tic Tac Toe.

Total game positions: 5,478
'''
from games import TicTacToe
from utils import ZobristHashing

zobrist_hash = ZobristHashing(n_positions=9, n_pieces=2)

def count_positions(game, hashed_boards):
    board_hash = zobrist_hash(game.board)
    hashed_boards.add(board_hash)
    for move in game.legal_moves():
        new_game = game.copy()
        new_game.make_move(move)
        count_positions(new_game, hashed_boards)

game = TicTacToe()
hashed_boards = set()
count_positions(game, hashed_boards)
print('Total game positions: {}'.format(len(hashed_boards)))
