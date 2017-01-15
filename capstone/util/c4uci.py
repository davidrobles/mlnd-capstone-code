from __future__ import division, print_function, unicode_literals
from capstone.game import Connect4 as C4


def load_instance(instance):
    '''
    Loads a position from the UCI Connect 4 database:

    https://archive.ics.uci.edu/ml/machine-learning-databases/connect-4/connect-4.names

    Returns a tuple with an instance of a Connect4 game with that position, and the
    outcome for the first player under perfect play.
    '''
    tokens = instance.split(',')
    cells = tokens[:-1]
    outcome = tokens[-1]
    cell_map = {'x': 'X', 'o': 'O', 'b': '-'}
    board = [[' '] * C4.COLS for row in range(C4.ROWS)]
    for ix, cell in enumerate(cells):
        row = C4.ROWS - (ix % C4.ROWS) - 1
        col = ix // C4.ROWS
        board[row][col] = cell_map[cell]
    return C4(board), outcome
