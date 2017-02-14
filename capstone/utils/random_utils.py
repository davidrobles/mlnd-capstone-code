import numpy as np


def check_random_state(seed):
    if seed is None or isinstance(seed, int):
        return np.random.RandomState(seed)
    elif isinstance(seed, np.random.RandomState):
        return seed
    raise ValueError('Seed should be None, int or np.random.RandomState')
