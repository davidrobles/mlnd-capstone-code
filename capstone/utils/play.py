from __future__ import print_function
import random


def play_match(game, players, verbose=True):
    """Plays a match between the given players"""
    if verbose:
        print(game)
    while not game.is_over():
        cur_player = players[game.cur_player()]
        move = cur_player.choose_move(game.copy())
        game.make_move(move)
        if verbose:
            print(game)


def play_series(game, players, n_matches=100, alternate=False, verbose=True):
    """Plays a series of 'n_matches' matches between the given players"""
    stats = {'p1win': 0, 'p2win': 0, 'draw': 0}
    match_players = [players[0], players[1]]
    for n_match in range(n_matches):
        print('Match {}:'.format(n_match), end=' ')
        play_match(game, match_players, verbose=False)
        stats[game.outcome] += 1
        print(game.outcomes())
        game.reset()
        if alternate:
            match_players[0], match_players[1] = match_players[1], match_players[0]
    print(stats)
