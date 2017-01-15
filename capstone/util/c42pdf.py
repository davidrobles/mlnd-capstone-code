from __future__ import division
import subprocess
import tempfile


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
        filename = '/Users/drobles/Desktop/c4.pdf'
        C42PDF(board, filename).create()
    '''

    def __init__(self, board, filename):
        self.board = board
        self.filename = filename

    def create(self):
        self._tf_ps = tempfile.NamedTemporaryFile()
        self._draw_background()
        self._draw_stones()
        self._create_pdf()

    def _draw_background(self):
        f = self._tf_ps
        def _bg_helper():
            f.write('newpath\n')
            f.write('10 10 moveto\n')
            f.write('0 %f rlineto\n' % (ROWS * CELL_SIZE))
            f.write('%f 0 rlineto\n' % (COLS * CELL_SIZE))
            f.write('0 -%f rlineto\n' % (ROWS * CELL_SIZE))
            f.write('-%f 0 rlineto\n' % (COLS * CELL_SIZE))
            f.write('closepath\n')
        # fill
        _bg_helper()
        f.write('%s setrgbcolor\n' % BG_COLOR)
        f.write('fill\n')
        # stroke
        _bg_helper()
        f.write('0 setgray\n')
        f.write('stroke\n')

    def _draw_stones(self):
        f = self._tf_ps
        offset = (CELL_SIZE // 2) + OFFSET
        for ri, row in enumerate(reversed(self.board)):
            for ci, col in enumerate(row):
                f.write('%s setrgbcolor\n' % COLORS[col])
                arc = (ci * CELL_SIZE + offset, ri * CELL_SIZE + offset, CELL_SIZE * 0.4)
                f.write('%d %d %d 0 360 arc fill\n' % arc)
                f.write('0 setgray\n')
                f.write('%d %d %d 0 360 arc stroke\n' % arc)

    def _create_pdf(self):
        self._tf_ps.write('showpage')
        self._tf_ps.flush()
        self.tf_updf = tempfile.NamedTemporaryFile()
        subprocess.call(['ps2pdf', self._tf_ps.name, self.tf_updf.name])
        self._tf_ps.close()
        subprocess.call(["pdfcrop", self.tf_updf.name, self.filename])
        self.tf_updf.close()


def c42pdf(board, filename):
    return C42PDF(board, filename).create()
