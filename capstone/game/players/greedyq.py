class GreedyQ(object):
    '''
    Selects a greedy move based on a given Q-function.
    '''

    def __init__(self, qf):
        self.qf = qf

    def choose_move(self, game):
        game_moves = [(game, move) for move in game.legal_moves()]
        _, best_move = max(game_moves, key=lambda gm: self.qf[gm])
        # check this works fine
        return best_move
