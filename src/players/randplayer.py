import random


class RandPlayer(object):

    def chooseMove(self, game):
        return random.choice(game.legal_moves())

    def __str__(self):
        return 'Random'
