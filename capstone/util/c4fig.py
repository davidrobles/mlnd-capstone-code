import subprocess

letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
letters = [x.upper() for x in letters]

board = [[' ', ' ', '1', ' ', ' ', ' ', ' '],
         [' ', ' ', '2', ' ', '1', ' ', ' '],
         [' ', ' ', '2', '2', '1', '1', '1'],
         [' ', ' ', '1', '1', '2', '2', '2'],
         [' ', '1', '2', '2', '1', '2', '2'],
         [' ', '2', '1', '2', '1', '2', '1']]

colors = {
	'1': '0.72 0.14 0.19',
	'2': '0.16 0.42 0.72',
	' ': '1.00 1.00 1.00'
}
X_OFFSET = 17.0
ROWS = len(board)
COLS = len(board[0])
CELL_SIZE = 20
OFFSET = 10
LETTERS = False
PATH = '/Users/drobles/Desktop/'
FILENAME = 'c4'


class C4Fig(object):

    def __init__(self):
        self.f = open(PATH + FILENAME + '.ps', 'w')
        self.draw_background()
        self.draw_stones()
        self.end()

    def draw_background(self):
        self.f.write('newpath\n')
        self.f.write('10 10 moveto\n')
        self.f.write('0 %f rlineto\n' % (ROWS * CELL_SIZE))
        self.f.write('%f 0 rlineto\n' % (COLS * CELL_SIZE))
        self.f.write('0 -%f rlineto\n' % (ROWS * CELL_SIZE))
        self.f.write('-%f 0 rlineto\n' % (COLS * CELL_SIZE))
        self.f.write('closepath\n')
        self.f.write('0.9 setgray\n')
        self.f.write('fill\n')

        self.f.write('newpath\n')
        self.f.write('10 10 moveto\n')
        self.f.write('0 %f rlineto\n' % (ROWS * CELL_SIZE))
        self.f.write('%f 0 rlineto\n' % (COLS * CELL_SIZE))
        self.f.write('0 -%f rlineto\n' % (ROWS * CELL_SIZE))
        self.f.write('-%f 0 rlineto\n' % (COLS * CELL_SIZE))
        self.f.write('closepath\n')
        self.f.write('0 setgray\n')
        self.f.write('stroke\n')

    def draw_stones(self):
        for ri, row in enumerate(reversed(board)):
            for ci, col in enumerate(row):
                self.f.write('%s setrgbcolor\n' % colors[col])
                arc = (ci * CELL_SIZE + (CELL_SIZE / 2) + OFFSET, ri * CELL_SIZE + (CELL_SIZE / 2) + OFFSET, CELL_SIZE * 0.35)
                self.f.write('%d %d %d 0 360 arc fill\n' % arc)
                self.f.write('0 setgray\n')
                self.f.write('%d %d %d 0 360 arc stroke\n' % arc)

    def end(self):
        self.f.write('showpage')
        self.f.flush()
        self.f.close()
        subprocess.call(["ps2pdf", PATH + FILENAME + ".ps", PATH + FILENAME + ".pdf"])
        subprocess.call(["pdfcrop", PATH + FILENAME + ".pdf", PATH + FILENAME + "-crop.pdf"])
        subprocess.call(["rm", PATH + FILENAME + ".ps"])
        subprocess.call(["rm", PATH + FILENAME + ".pdf"])

C4Fig()
