from __future__ import division, unicode_literals
import pandas as pd
from capstone.game import Connect4 as C4


def load_uci_c4():
    '''
    Returns a Pandas Dataframe of the UCI Connect 4 dataset

    https://archive.ics.uci.edu/ml/machine-learning-databases/connect-4/connect-4.names
    '''

    def column_name(i):
        if i == 42:
            return 'outcome'
        row = chr(ord('a') + (i // C4.ROWS))
        col = (i % C4.ROWS) + 1
        return '{row}{col}'.format(row=row, col=col)

    column_names = [column_name(i) for i in range(43)]
    return pd.read_csv('datasets/uci_c4.csv', header=None, names=column_names)
