from capstone.util import c42pdf


board = [[' ', ' ', '1', ' ', ' ', ' ', ' '],
         [' ', ' ', '2', ' ', '1', ' ', ' '],
         [' ', ' ', '2', '2', '1', '1', '1'],
         [' ', ' ', '1', '1', '2', '2', '2'],
         [' ', '1', '2', '2', '1', '2', '2'],
         [' ', '2', '1', '2', '1', '2', '1']]
filename = '/Users/drobles/Desktop/c4.pdf'
c42pdf(board, filename)
