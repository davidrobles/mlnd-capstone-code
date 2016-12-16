from __future__ import print_function
import random

def play_random_game(game):
    """Plays a game taking uniformly random moves"""
    print(game)
    while not game.is_over():
        rand_move = random.choice(game.legal_moves())
        game.make_move(rand_move)
        print(game)


def play_series(game, players, n_matches=100):
    game = game.copy()
    stats = {'p1_wins': 0, 'p2_wins': 0, 'draws': 0}
    for __ in range(n_matches):
        while not game.is_over():
            cur_player = players[game.cur_player()]
            move = cur_player.chooseMove(game.copy())
            game.make_move(move)
        outcomes = game.outcomes()
        if outcomes[0] == 'W':
            stats['p1_wins'] += 1
        elif outcomes[1] == 'W':
            stats['p2_wins'] += 1
        else:
            stats['draws'] += 1
        game.reset()
    print(stats)
