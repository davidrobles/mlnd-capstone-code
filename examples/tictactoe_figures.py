from capstone.util import tic2pdf


board = [[' ', ' ', '1'],
         [' ', ' ', '2'],
         [' ', '2', '1']]
filename = '/Users/drobles/Desktop/tic.pdf'
tic2pdf(board, filename)
