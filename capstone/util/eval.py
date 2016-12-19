def default_util_func(game, player):
    '''
    Returns the utility at the end of the game for the given player:
    1 for win, 0 for draw, and -1 for loss
    '''
    utilities = {'W': 1.0, 'L': -1.0, 'D': 0.0}
    outcome = game.outcome(player)
    return utilities[outcome]
