def check_random_state(seed):
    import numpy as np
    if seed is None or isinstance(seed, int):
        return np.random.RandomState(seed)
    elif isinstance(seed, np.random.RandomState):
        return seed
    raise ValueError('Seed should be None, int or np.random.RandomState')


from .print_util import print_header
from .aec import print_aec, str_aec
from .c42pdf import c42pdf
from .tic2pdf import tic2pdf
from .eval import utility
from .play import play_match, play_series
from .zobrist import ZobristHashing
