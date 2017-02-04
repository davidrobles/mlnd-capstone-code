from __future__ import division, print_function
from capstone.datasets import load_uci_c4
from capstone.util import print_header

df = load_uci_c4()
outcomes = df.loc[:, 'outcome']

print_header('Dataset')
print(df, end='\n\n')

print_header('Number of instances')
print(df.shape[0], end='\n\n')

print_header('Outcomes')
print(outcomes.value_counts(), end='\n\n')

print_header('Normalized Outcomes')
print(outcomes.value_counts(normalize=True))
