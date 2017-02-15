'''
Exploration of the UCI C4 dataset:

- Number of instances.
- Outcomes counts.
- Normalized outcomes counts.
'''
from __future__ import print_function
from capstone.datasets import load_uci_c4
from capstone.utils import print_header

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
