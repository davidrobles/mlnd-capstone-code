
def norm_tic_board(state):
    import numpy as np
    m = {'X': 1.0, ' ': 0.0, 'O': -1.0}
    return np.array([[m[col] for row in state.board for col in row]])

from .print_util import print_header
from .aec import print_aec, str_aec
from .c42pdf import c42pdf
from .tic2pdf import tic2pdf
from .eval import utility
from .play import play_match, play_series
from .random_utils import check_random_state
from .zobrist import ZobristHashing
