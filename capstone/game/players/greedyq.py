class GreedyQ(object):
    '''
    Selects a greedy move based on a given Q-function.
    '''

    def __init__(self, qfunction):
        self.qfunction = qfunction

    def choose_move(self, game):
        game_moves = [(game, move) for move in game.legal_moves()]
        _, best_move = max(game_moves, key=lambda gm: self.qfunction[gm])
        return best_move
