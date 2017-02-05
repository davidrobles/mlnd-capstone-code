from __future__ import division, unicode_literals
import subprocess
import tempfile


BG_COLOR = '1.0 1.0 1.0'
COLORS = {
    'X': '0.85 0.12 0.15',
    'O': '0.21 0.60 0.83',
    ' ': '0.83 0.60 0.32'
}
X_OFFSET = 17.0
ROWS = 3
COLS = 3
CELL_SIZE = 20
OFFSET = 10


class Tic2PDF(object):
    '''
    Generates a PDF of a Tic-Tac-Toe board.

    Example:

        filename = 'c4.pdf'
        board = [[' ', ' ', 'X'],
                 [' ', ' ', 'O'],
                 [' ', ' ', 'X']]
        Tic2PDF(filename, board).create()
    '''

    def __init__(self, filename, board):
        self.filename = filename
        self.board = board

    def create(self):
        self._tf_ps = tempfile.NamedTemporaryFile()
        self._draw_lines()
        self._draw_pieces()
        self._create_pdf()

    def _draw_lines(self):
        f = self._tf_ps
        f.write('newpath\n')
        # horizontal
        f.write('10 %f moveto\n' % (CELL_SIZE + 10))
        f.write('60 0 rlineto\n')
        f.write('10 50 moveto\n')
        f.write('60 0 rlineto\n')
        # vertical
        f.write('30 10 moveto\n')
        f.write('0 60 rlineto\n')
        f.write('50 10 moveto\n')
        f.write('0 60 rlineto\n')
        f.write('closepath\n')
        # stroke
        f.write('0 setgray\n')
        f.write('1 setlinewidth\n')
        f.write('stroke\n')

    def _draw_pieces(self):
        f = self._tf_ps
        offset = (CELL_SIZE // 2) + OFFSET
        for ri, row in enumerate(reversed(self.board)):
            for ci, col in enumerate(row):
                f.write('2 setlinewidth\n')
                if col == 'X':
                    # /
                    f.write('newpath\n')
                    f.write('%f %f moveto\n' % ((ci * CELL_SIZE) + 10 + 4, (ri * CELL_SIZE) + 10 + 4))
                    f.write('12 12 rlineto\n')
                    f.write('closepath\n')
                    f.write('%s setrgbcolor\n' % COLORS[col])
                    f.write('stroke\n')
                    # \
                    f.write('newpath\n')
                    f.write('%f %f moveto\n' % ((ci * CELL_SIZE) + 10 + 16, (ri * CELL_SIZE) + 10 + 4))
                    f.write('-12 12 rlineto\n')
                    f.write('closepath\n')
                    f.write('%s setrgbcolor\n' % COLORS[col])
                    f.write('stroke\n')
                elif col == 'O':
                    f.write('%s setrgbcolor\n' % COLORS[col])
                    arc = (ci * CELL_SIZE + offset, ri * CELL_SIZE + offset, CELL_SIZE * 0.38)
                    f.write('%d %d %d 0 360 arc stroke\n' % arc)

    def _create_pdf(self):
        self._tf_ps.write('showpage')
        self._tf_ps.flush()
        self.tf_updf = tempfile.NamedTemporaryFile()
        subprocess.call(['ps2pdf', self._tf_ps.name, self.tf_updf.name])
        self._tf_ps.close()
        subprocess.call(["pdfcrop", self.tf_updf.name, self.filename])
        self.tf_updf.close()


def tic2pdf(filename, board):
    return Tic2PDF(filename, board).create()
