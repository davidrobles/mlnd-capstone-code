from __future__ import print_function
from .aec import print_aec, str_aec
from .c42pdf import c42pdf
from .tic2pdf import tic2pdf
from .eval import utility
from .play import play_match, play_series
from .zobrist import ZobristHashing


def print_header(text):
    l = len(text) + 2
    print('-' * l)
    print(' {} '.format(text))
    print('-' * l, end='\n\n')
