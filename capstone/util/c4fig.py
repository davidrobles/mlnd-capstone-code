import subprocess

letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
letters = [x.upper() for x in letters]

# board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
#          [' ', ' ', ' ', ' ', ' ', ' ', ' '],
#          [' ', ' ', ' ', ' ', ' ', ' ', ' '],
#          [' ', ' ', ' ', ' ', ' ', ' ', ' '],
#          [' ', ' ', ' ', ' ', ' ', ' ', ' '],
#          [' ', ' ', ' ', ' ', ' ', ' ', ' ']]

# win by blue

board = [[' ', ' ', '1', ' ', ' ', ' ', ' '],
         [' ', ' ', '2', ' ', '1', ' ', ' '],
         [' ', ' ', '2', '2', '1', '1', '1'],
         [' ', ' ', '1', '1', '2', '2', '2'],
         [' ', '1', '2', '2', '1', '2', '2'],
         [' ', '2', '1', '2', '1', '2', '1']]

# win by red

# board = [[' ', ' ', ' ', '2', '1', ' ', ' '],
#          [' ', ' ', '2', '1', '1', ' ', ' '],
#          [' ', ' ', '1', '2', '2', ' ', ' '],
#          [' ', '1', '2', '2', '1', ' ', ' '],
#          ['2', '1', '1', '1', '2', ' ', ' '],
#          ['2', '1', '1', '2', '2', ' ', ' ']]

# draw

# board = [['1', '1', '2', '1', '1', '2', '2'],
#          ['2', '1', '1', '2', '2', '1', '1'],
#          ['1', '2', '1', '1', '1', '2', '2'],
#          ['2', '1', '2', '2', '2', '1', '1'],
#          ['1', '2', '2', '1', '1', '2', '2'],
#          ['2', '1', '2', '2', '1', '1', '2']]

X_OFFSET = 17.0
ROWS = len(board)
COLS = len(board[0])
CELL_SIZE = 20
OFFSET = 10
LETTERS = False
PATH = '/Users/drobles/Desktop/'
FILENAME = 'c4'
file = open(PATH + FILENAME + '.ps', 'w')

# BACKGROUND

file.write('newpath\n')
file.write('10 10 moveto\n')
file.write('0 %f rlineto\n' % (ROWS * CELL_SIZE))
file.write('%f 0 rlineto\n' % (COLS * CELL_SIZE))
file.write('0 -%f rlineto\n' % (ROWS * CELL_SIZE))
file.write('-%f 0 rlineto\n' % (COLS * CELL_SIZE))
file.write('closepath\n')
file.write('0.9 setgray\n')
file.write('fill\n')

file.write('newpath\n')
file.write('10 10 moveto\n')
file.write('0 %f rlineto\n' % (ROWS * CELL_SIZE))
file.write('%f 0 rlineto\n' % (COLS * CELL_SIZE))
file.write('0 -%f rlineto\n' % (ROWS * CELL_SIZE))
file.write('-%f 0 rlineto\n' % (COLS * CELL_SIZE))
file.write('closepath\n')
file.write('0 setgray\n')
file.write('stroke\n')

colors = {
	'1': '0.72 0.14 0.19',
	'2': '0.16 0.42 0.72',
	' ': '1.00 1.00 1.00'
}

# STONES

for ri, row in enumerate(reversed(board)):
    for ci, col in enumerate(row):
		file.write('%s setrgbcolor\n' % colors[col])
		file.write('%d %d %d 0 360 arc fill\n' % (ci * CELL_SIZE + (CELL_SIZE / 2) + OFFSET, ri * CELL_SIZE + (CELL_SIZE / 2) + OFFSET, CELL_SIZE * 0.35))
		file.write('0 setgray\n')
		file.write('%d %d %d 0 360 arc stroke\n' % (ci * CELL_SIZE + (CELL_SIZE / 2) + OFFSET, ri * CELL_SIZE + (CELL_SIZE / 2) + OFFSET, CELL_SIZE * 0.35))

file.write('showpage')
file.flush()
file.close()

subprocess.call(["ps2pdf", PATH + FILENAME + ".ps", PATH + FILENAME + ".pdf"])
subprocess.call(["pdfcrop", PATH + FILENAME + ".pdf", PATH + FILENAME + "-crop.pdf"])
subprocess.call(["rm", PATH + FILENAME + ".ps"])
subprocess.call(["rm", PATH + FILENAME + ".pdf"])
