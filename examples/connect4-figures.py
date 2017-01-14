from capstone.util.c42pdf import C42PDF


board = [[' ', ' ', '1', ' ', ' ', ' ', ' '],
         [' ', ' ', '2', ' ', '1', ' ', ' '],
         [' ', ' ', '2', '2', '1', '1', '1'],
         [' ', ' ', '1', '1', '2', '2', '2'],
         [' ', '1', '2', '2', '1', '2', '2'],
         [' ', '2', '1', '2', '1', '2', '1']]
filename = '/Users/drobles/Desktop/c4.pdf'
C42PDF(board, filename).create()
