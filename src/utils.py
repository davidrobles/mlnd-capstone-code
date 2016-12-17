from __future__ import print_function
import random


def play_match(game, players, verbose=True):
    """Plays a match between the given players"""
    game = game.copy()
    if verbose:
        print(game)
    while not game.is_over():
        cur_player = players[game.cur_player]
        move = cur_player.choose_move(game.copy())
        game.make_move(move)
        if verbose:
            print(game)
    return game.outcomes()


def play_series(game, players, n_matches=100, verbose=True):
    """Plays a series of 'n_matches' matches between the given players"""
    stats = {'p1_wins': 0, 'p2_wins': 0, 'draws': 0}
    for n_match in range(n_matches):
        print('Match {}:'.format(n_match), end=' ')
        outcomes = play_match(game, players, verbose=False)
        if outcomes[0] == 'W':
            stats['p1_wins'] += 1
        elif outcomes[1] == 'W':
            stats['p2_wins'] += 1
        else:
            stats['draws'] += 1
        print(outcomes)
        game.reset()
    print(stats)


def default_util_func(game, player):
    if game.outcomes()[player] == 'W':
        return 1.0
    elif game.outcomes()[player] == 'L':
        return -1.0
    else:
        return 0.0
