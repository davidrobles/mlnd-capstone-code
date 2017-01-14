from __future__ import print_function
from capstone.game import Connect4 as C4

line = 'b,b,b,b,b,b,b,b,b,b,b,b,x,o,b,b,b,b,x,o,x,o,x,o,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,win'
values = line.split(',')
cells = values[:-1]
outcome = values[-1]
m = {'x': 'X', 'o': 'O', 'b': '-'}
board = [[' '] * C4.COLS for row in range(C4.ROWS)]

for ix, cell in enumerate(cells):
    row = C4.ROWS - 1 - (ix % C4.ROWS)
    col = ix / C4.ROWS
    board[row][col] = m[cell]


b = C4(board)
print(b)
