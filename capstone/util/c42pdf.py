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
        full_path = '/Users/drobles/Desktop/'
        filename = 'c4'
        C42PDF(board, full_path, filename).create()
    '''

    def __init__(self, board, filename):
        self.board = board
        self.filename = filename

    def create(self):
        self.tf = tempfile.NamedTemporaryFile()
        self._draw_background()
        self._draw_stones()
        self._create_pdf()

    def _draw_background(self):
        self.tf.write('newpath\n')
        self.tf.write('10 10 moveto\n')
        self.tf.write('0 %f rlineto\n' % (ROWS * CELL_SIZE))
        self.tf.write('%f 0 rlineto\n' % (COLS * CELL_SIZE))
        self.tf.write('0 -%f rlineto\n' % (ROWS * CELL_SIZE))
        self.tf.write('-%f 0 rlineto\n' % (COLS * CELL_SIZE))
        self.tf.write('closepath\n')
        self.tf.write('%s setrgbcolor\n' % BG_COLOR)
        self.tf.write('fill\n')

        self.tf.write('newpath\n')
        self.tf.write('10 10 moveto\n')
        self.tf.write('0 %f rlineto\n' % (ROWS * CELL_SIZE))
        self.tf.write('%f 0 rlineto\n' % (COLS * CELL_SIZE))
        self.tf.write('0 -%f rlineto\n' % (ROWS * CELL_SIZE))
        self.tf.write('-%f 0 rlineto\n' % (COLS * CELL_SIZE))
        self.tf.write('closepath\n')
        self.tf.write('0 setgray\n')
        self.tf.write('stroke\n')

    def _draw_stones(self):
        for ri, row in enumerate(reversed(self.board)):
            for ci, col in enumerate(row):
                self.tf.write('%s setrgbcolor\n' % COLORS[col])
                arc = (
                    ci * CELL_SIZE + (CELL_SIZE / 2) + OFFSET,
                    ri * CELL_SIZE + (CELL_SIZE / 2) + OFFSET,
                    CELL_SIZE * 0.4
                )
                self.tf.write('%d %d %d 0 360 arc fill\n' % arc)
                self.tf.write('0 setgray\n')
                self.tf.write('%d %d %d 0 360 arc stroke\n' % arc)

    def _create_pdf(self):
        self.tf.write('showpage')
        self.tf.flush()
        # self.f.close()
        self.tf_uncropped = tempfile.NamedTemporaryFile()
        subprocess.call(['ps2pdf', self.tf.name, self.tf_uncropped.name])
        subprocess.call(["pdfcrop", self.tf_uncropped.name, self.filename])
