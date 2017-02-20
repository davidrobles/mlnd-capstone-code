from __future__ import print_function
from ...utils import print_header


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
    Plays a series of 'n_matches' of a 'game' between
    the given 'players'.
    """
    print_header('Series')
    print('Game:', game.name)
    print('Players:', players)
    print('No. Matches: %d\n' % n_matches)
    counters = {'W': 0, 'L': 0, 'D': 0}
    for n_match in range(1, n_matches + 1):
        print('Match %d/%d:' % (n_match, n_matches), end=' ')
        new_game = game.copy()
        play_match(new_game, players, verbose=False)
        outcomes = new_game.outcomes()
        counters[outcomes[0]] += 1
        print(outcomes)
    print('\nOutcomes:', counters)
