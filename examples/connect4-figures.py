from capstone.util.c42pdf import C42PDF


board = [[' ', ' ', '1', ' ', ' ', ' ', ' '],
         [' ', ' ', '2', ' ', '1', ' ', ' '],
         [' ', ' ', '2', '2', '1', '1', '1'],
         [' ', ' ', '1', '1', '2', '2', '2'],
         [' ', '1', '2', '2', '1', '2', '2'],
         [' ', '2', '1', '2', '1', '2', '1']]
full_path = '/Users/drobles/Desktop/'
filename = 'c4'
C42PDF(board, full_path, filename).create()
