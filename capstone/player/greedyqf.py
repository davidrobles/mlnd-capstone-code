import random


class GreedyQF(object):
    '''
    Takes a greedy action based on a given q-valeu function
    '''

    def __init__(self, qf):
        self.qf = qf

    def choose_move(self, game):
        best_value = -100000
        best_move = None
        for move in game.legal_moves():
            if (game, move) not in self.qf:
                continue
            temp_value = self.qf[(game, move)]
            if temp_value > best_value:
                best_value = temp_value
                best_move = move
        if best_move is None:
            return random.choice(game.legal_moves())
        return best_move
