from __future__ import division, print_function
import random
from capstone.datasets import load_uci_c4
from capstone.game.games import Connect4 as C4
from capstone.game.utils import c42pdf

def series_to_game(series):
    '''Converts a Pandas Series to a Connect 4 game'''
    cell_map = {'x': 'X', 'o': 'O', 'b': '-'}
    board = [[' '] * C4.COLS for row in range(C4.ROWS)]
    cells = series.iloc[:-1]
    outcome = series.iloc[-1]
    for ix, cell in enumerate(cells):
        row = C4.ROWS - (ix % C4.ROWS) - 1
        col = ix // C4.ROWS
        board[row][col] = cell_map[cell]
    return C4(board), outcome

# Load UCI Connect 4 dataset
df = load_uci_c4()

# Select the instances of the dataset
ixs = [1, 5, 10, 20, 567]

# Generate pdfs of the boards
for i in ixs:
    row = df.iloc[i]
    c4, outcome = series_to_game(row)
    filename = 'figures/c4_exploration_{i}_{outcome}.pdf'.format(i=i, outcome=outcome)
    c42pdf(filename, c4.board)
