from __future__ import division, print_function
import random
from capstone.util import c42pdf
from capstone.util.c4uci import load_instance

FILENAME = 'datasets/connect-4.data'

games = []
outcomes = []

with open(FILENAME) as f:
    for i, line in enumerate(f, 1):
        game, outcome = load_instance(line)
        outcomes.append(outcome)
        games.append(game)

for i in range(1, 10 + 1):
    ix = random.randint(0, len(games) - 1)
    game = games[ix]
    outcome = outcomes[ix]
    filename = 'figures/c4_exploration_{i}_{outcome}.pdf'.format(i=i, outcome=outcome)
    c42pdf(game.board, filename)
