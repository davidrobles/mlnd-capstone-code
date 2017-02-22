import random


class GreedyQF(object):
    '''
    Takes a greedy action based on a given q-value function
    '''

    def __init__(self, qf):
        self.qf = qf

    def choose_move(self, game):
        game_moves = [(game, move) for move in game.legal_moves()]
        _, best_move = max(game_moves, key=lambda gm: self.qf[gm])
        return best_move
