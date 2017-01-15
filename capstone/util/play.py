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


def play_series(game, players, n_matches=100):
    """
    Plays a series of 'n_matches' matches of a 'game' between
    the given 'players'.
    """
    print('--------')
    print(' Series ')
    print('--------\n')
    print('No. Matches: {}'.format(n_matches))
    print('Game: {}'.format(game.name))
    print('Players: {}\n'.format(players))
    for n_match in range(1, n_matches + 1):
        print('Match {}:'.format(n_match), end=' ')
        new_game = game.copy()
        play_match(new_game, players, verbose=False)
        print(new_game.outcomes())
