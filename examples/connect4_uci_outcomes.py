from __future__ import division, print_function
import pandas as pd
from sklearn.linear_model import LinearRegression
from capstone.game import Connect4 as C4
from capstone.util import print_header

FILENAME = 'datasets/connect-4.data'

def column_name(i):
    if i == 42:
        return 'outcome'
    row = chr(ord('a') + (i // C4.ROWS))
    col = (i % C4.ROWS) + 1
    return '{row}{col}'.format(row=row, col=col)

column_names = [column_name(i) for i in range(43)]
df = pd.read_csv(FILENAME, header=None, names=column_names)
outcomes = df.loc[:, 'outcome']

print_header('Dataset')
print(df, end='\n\n')

print_header('Number of instances')
print(df.shape[0], end='\n\n')

print_header('Outcomes')
print(outcomes.value_counts(), end='\n\n')

print_header('Normalized Outcomes')
print(outcomes.value_counts(normalize=True))
