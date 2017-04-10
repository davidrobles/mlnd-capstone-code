from __future__ import division, unicode_literals
import pandas as pd
from capstone.game.games import Connect4 as C4


def load_dataframe():
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


def series_to_game(series):
    '''Converts a Pandas Series to a Connect 4 game'''
    cell_map = {'x': 'X', 'o': 'O', 'b': '-'}
    board = [[' '] * C4.COLS for row in range(C4.ROWS)]
    cells = series.iloc[:-1]
    outcome = series.iloc[-1]
    for ix, cell in enumerate(cells):
        row = C4.ROWS - (ix % C4.ROWS) - 1
        col = ix // C4.ROWS
        board[row][col] = cell_map[cell]
    return C4(board), outcome


_df = load_dataframe()


def get_random_game():
    sample_df = _df.sample()
    row = sample_df.iloc[0]
    game, _ = series_to_game(row)
    return game

def get_random_win_game():
    sample_df = _df.loc[_df['outcome'] == 'win'].sample()
    row = sample_df.iloc[0]
    game, _ = series_to_game(row)
    return game
