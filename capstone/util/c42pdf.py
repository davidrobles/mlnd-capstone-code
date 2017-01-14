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
        self.tf_ps = tempfile.NamedTemporaryFile()
        self._draw_background()
        self._draw_stones()
        self._create_pdf()

    def _draw_background(self):
        def _bg_helper():
            self.tf_ps.write('newpath\n')
            self.tf_ps.write('10 10 moveto\n')
            self.tf_ps.write('0 %f rlineto\n' % (ROWS * CELL_SIZE))
            self.tf_ps.write('%f 0 rlineto\n' % (COLS * CELL_SIZE))
            self.tf_ps.write('0 -%f rlineto\n' % (ROWS * CELL_SIZE))
            self.tf_ps.write('-%f 0 rlineto\n' % (COLS * CELL_SIZE))
            self.tf_ps.write('closepath\n')
        # fill
        _bg_helper()
        self.tf_ps.write('%s setrgbcolor\n' % BG_COLOR)
        self.tf_ps.write('fill\n')
        # stroke
        _bg_helper()
        self.tf_ps.write('0 setgray\n')
        self.tf_ps.write('stroke\n')

    def _draw_stones(self):
        for ri, row in enumerate(reversed(self.board)):
            for ci, col in enumerate(row):
                self.tf_ps.write('%s setrgbcolor\n' % COLORS[col])
                arc = (
                    ci * CELL_SIZE + (CELL_SIZE / 2) + OFFSET,
                    ri * CELL_SIZE + (CELL_SIZE / 2) + OFFSET,
                    CELL_SIZE * 0.4
                )
                self.tf_ps.write('%d %d %d 0 360 arc fill\n' % arc)
                self.tf_ps.write('0 setgray\n')
                self.tf_ps.write('%d %d %d 0 360 arc stroke\n' % arc)

    def _create_pdf(self):
        self.tf_ps.write('showpage')
        self.tf_ps.flush()
        self.tf_updf = tempfile.NamedTemporaryFile()
        subprocess.call(['ps2pdf', self.tf_ps.name, self.tf_updf.name])
        self.tf_ps.close()
        subprocess.call(["pdfcrop", self.tf_updf.name, self.filename])
        self.tf_updf.close()


def c42pdf(board, filename):
    return C42PDF(board, filename).create()
