from __future__ import print_function
import random
from players import RandPlayer

def play_random_game(game):
    """Plays a game taking uniformly random moves"""
    print(play_match(game, [RandPlayer(), RandPlayer()]))

def play_match(game, players, verbose=True):
    """Plays a match between the given players"""
    game = game.copy()
    if verbose:
        print(game)
    while not game.is_over():
        cur_player = players[game.cur_player()]
        move = cur_player.chooseMove(game.copy())
        game.make_move(move)
        if verbose:
            print(game)
    return game.outcomes()

def play_series(game, players, n_matches=100):
    """Plays a series of 'n_matches' matches between the given players"""
    stats = {'p1_wins': 0, 'p2_wins': 0, 'draws': 0}
    for __ in range(n_matches):
        outcomes = play_match(game, players)
        if outcomes[0] == 'W':
            stats['p1_wins'] += 1
        elif outcomes[1] == 'W':
            stats['p2_wins'] += 1
        else:
            stats['draws'] += 1
        game.reset()
    print(stats)
