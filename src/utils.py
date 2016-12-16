import random

def play_random_game(game):
    """Plays a game taking uniformly random moves"""
    # print(game)
    # while not game.is_over():
    #     rand_move = random.choice(game.legal_moves())
    #     game.make_move(rand_move)
    #     # game.make_move(2)
    #     print(game)

    print(game)
    rand_move = random.choice(game.legal_moves())
    game.make_move(rand_move)
    print(game)

    rand_move = random.choice(game.legal_moves())
    game.make_move(rand_move)
    print(game)
