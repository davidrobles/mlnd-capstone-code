from __future__ import print_function
from capstone.game import Connect4 as C4

ROWS = 6
COLS = 7

line = 'b,b,b,b,b,b,b,b,b,b,b,b,x,o,b,b,b,b,x,o,x,o,x,o,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,win'
values = line.split(',')
cells = values[:-1]
outcome = values[-1]

board = [[' '] * COLS for row in range(ROWS)]

for ix, c in enumerate(cells):
    row = C4.ROWS - 1 - (ix % ROWS)
    col = ix / ROWS
    if c == 'x':
        board[row][col] = 'X'
    elif c == 'o':
        board[row][col] = 'O'
    else:
        board[row][col] = '-'


b = C4(board)
print(b)
