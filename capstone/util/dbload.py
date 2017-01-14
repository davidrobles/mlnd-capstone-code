from __future__ import division, print_function, unicode_literals
from capstone.game import Connect4 as C4

line = 'b,b,b,b,b,b,b,b,b,b,b,b,x,o,b,b,b,b,x,o,x,o,x,o,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,win'
values = line.split(',')
cells = values[:-1]
outcome = values[-1]
m = {'x': 'X', 'o': 'O', 'b': '-'}
board = [[' '] * C4.COLS for row in range(C4.ROWS)]

for ix, cell in enumerate(cells):
    row = C4.ROWS - (ix % C4.ROWS) - 1
    col = ix // C4.ROWS
    board[row][col] = m[cell]

b = C4(board)
print(b)
