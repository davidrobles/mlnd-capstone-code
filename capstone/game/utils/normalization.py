import numpy as np


def normalize_board(board):
    m = {'X': 1.0, ' ': 0.0, 'O': -1.0}
    return np.array([[m[col] for row in board for col in row]])
