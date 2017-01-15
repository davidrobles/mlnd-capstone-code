from __future__ import print_function
from collections import Counter
from capstone.util.c4uci import load_instance

FILENAME = 'datasets/connect-4.data'

with open(FILENAME) as f:
    counter = Counter()
    for i, line in enumerate(f, 1):
        game, outcome = load_instance(line)
        counter[outcome] += 1
        if i == 1000:
            print(game)
            print(outcome)
            break
