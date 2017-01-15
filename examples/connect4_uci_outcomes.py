from __future__ import division, print_function
from collections import Counter
from capstone.util.c4uci import load_instance

FILENAME = 'datasets/connect-4.data'

outcomes = []

with open(FILENAME) as f:
    for i, line in enumerate(f, 1):
        _, outcome = load_instance(line)
        outcomes.append(outcome)
        if i % 1000 == 0:
            print(i)

counter = Counter(outcomes)
print('\n---------')
print(' Results')
print('---------\n')
print('total: {}'.format(len(outcomes)))
for outcome in ['win', 'loss', 'draw']:
    print('{outcome}: {count} ({pct:.2f}%)'.format(
        outcome=outcome,
        count=counter[outcome],
        pct=((counter[outcome] / len(outcomes)) * 100)
    ))
