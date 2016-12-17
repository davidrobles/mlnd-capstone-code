'''Calculates the number of different positions in Tic Tac Toe.

Total game positions: 5,478
'''
from games import TicTacToe
from players import RandPlayer
from utils import play_series, ZobristHashing


game = TicTacToe()
transp = set()
n_positions = 9
n_pieces = 2
zobrist = ZobristHashing(9, 2)

def traverse(game):
    global transp
    count = 0
    h = zobrist.hash(game.board)
    if h not in transp:
        count +=1
        transp.add(h)
    for move in game.legal_moves():
        new_game = game.copy()
        new_game.make_move(move)
        count += traverse(new_game)
    return count


count = traverse(game)
print('Total game positions: {}'.format(count))

