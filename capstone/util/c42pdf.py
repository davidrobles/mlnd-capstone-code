import subprocess

BG_COLOR = '0.00 0.50 0.77'
COLORS = { '1': '0.85 0.12 0.15', '2': '1.00 0.80 0.01', ' ': '0.90 0.90 0.90' }
X_OFFSET = 17.0
ROWS = 6
COLS = 7
CELL_SIZE = 20
OFFSET = 10


class C42PDF(object):
    '''
    Generates a PDF of the given Connect4 board.

    Example:

        board = [[' ', ' ', '1', ' ', ' ', ' ', ' '],
                 [' ', ' ', '2', ' ', '1', ' ', ' '],
                 [' ', ' ', '2', '2', '1', '1', '1'],
                 [' ', ' ', '1', '1', '2', '2', '2'],
                 [' ', '1', '2', '2', '1', '2', '2'],
                 [' ', '2', '1', '2', '1', '2', '1']]
        full_path = '/Users/drobles/Desktop/'
        filename = 'c4'
        C42PDF(board, full_path, filename).create()
    '''

    def __init__(self, board, full_path, filename):
        self.board = board
        self.full_path = full_path
        self.filename = filename
        self.full_filename = self.full_path + self.filename

    def create(self):
        self.f = open('%s.ps' % self.full_filename, 'w')
        self._draw_background()
        self._draw_stones()
        self._create_pdf()

    def _draw_background(self):
        self.f.write('newpath\n')
        self.f.write('10 10 moveto\n')
        self.f.write('0 %f rlineto\n' % (ROWS * CELL_SIZE))
        self.f.write('%f 0 rlineto\n' % (COLS * CELL_SIZE))
        self.f.write('0 -%f rlineto\n' % (ROWS * CELL_SIZE))
        self.f.write('-%f 0 rlineto\n' % (COLS * CELL_SIZE))
        self.f.write('closepath\n')
        self.f.write('%s setrgbcolor\n' % BG_COLOR)
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

    def _draw_stones(self):
        for ri, row in enumerate(reversed(self.board)):
            for ci, col in enumerate(row):
                self.f.write('%s setrgbcolor\n' % COLORS[col])
                arc = (
                    ci * CELL_SIZE + (CELL_SIZE / 2) + OFFSET,
                    ri * CELL_SIZE + (CELL_SIZE / 2) + OFFSET,
                    CELL_SIZE * 0.4
                )
                self.f.write('%d %d %d 0 360 arc fill\n' % arc)
                self.f.write('0 setgray\n')
                self.f.write('%d %d %d 0 360 arc stroke\n' % arc)

    def _create_pdf(self):
        self.f.write('showpage')
        self.f.flush()
        self.f.close()
        fn = self.full_filename
        subprocess.call(["ps2pdf", "%s.ps" % fn, "%s_.pdf" % fn])
        subprocess.call(["pdfcrop", "%s_.pdf" % fn, "%s.pdf" % fn])
        subprocess.call(["rm", "%s.ps" % fn])
        subprocess.call(["rm", "%s_.pdf" % fn])
