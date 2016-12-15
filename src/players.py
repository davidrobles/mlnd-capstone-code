from games import Player
from time import time
import random
import operator

class RandomPlayer(Player):

    def move(self, game, time_due=0):
        return random.randint(0, game.num_moves() - 1)

    def __str__(self):
        return 'Random'

class Minimax(Player):

    def hola(self):
        print("hol")

    def __init__(self, ef, max_depth):
        self.ef = ef
        self.max_depth = max_depth

    def __str__(self):
        return 'Minimax'

    def move(self, game, time_due=0):
        self.player = game.cur_player()
        return self.minimax(game, 0)[0]

    def minimax(self, game, cur_depth):
        if game.game_over() or cur_depth == self.max_depth:
            return [-1, self.ef.eval(game, self.player)]
        best_move = -1
#        best_score = -100000000 if game.cur_player() == self.player else 100000000
        if game.cur_player() == self.player:
            best_score = -100000000
        else:
            best_score = 100000000
        for move in range(0, game.num_moves()):
            new_game = game.copy()
            new_game.move(move)
            [_, cur_score] = self.minimax(new_game, cur_depth + 1)
            if game.cur_player == self.player:
                if cur_score > best_score:
                    best_score = cur_score
                    best_move = move
            elif cur_score < best_score:
                best_score = cur_score
                best_move = move
        return [best_move, best_score]

class Negamax(Player):

    def __init__(self, ef, max_depth):
        self.ef = ef
        self.max_depth = max_depth

    def __str__(self):
        return 'Negamax'

    def move(self, game, time_due=0):
        self.player = game.cur_player()
        return self.negamax(game, 0)[0]

    def negamax(self, game, cur_depth):
        if game.is_over() or cur_depth == self.max_depth:
            return [-1, self.ef.eval(game, self.player)]
        best_move = -1
        best_score = -100000000
        for move in range(0, game.num_moves()):
            new_game = game.copy()
            new_game.move(move)
            [_, cur_score] = self.negamax(new_game, cur_depth + 1)
            if cur_score > best_score:
                best_score = cur_score
                best_move = move
        return [best_move, best_score]

class ABNegamax(Player):

    def __init__(self, ef, max_depth):
        self.ef = ef
        self.max_depth = max_depth

    def __str__(self):
        return 'ABNegamax'

    def move(self, game, time_due=0):
        return self.abnegamax(game, 0, -100000000, 100000000)[0]

    def abnegamax(self, game, cur_depth, alpha, beta):
        if game.is_over() or cur_depth == self.max_depth:
            return [-1, self.ef.eval(game, game.cur_player())]
        best_move = -1
        best_score = -100000000
        for move in range(0, game.num_moves()):
            new_game = game.copy()
            new_game.move(move)
            [_, cur_score] = self.abnegamax(new_game, cur_depth + 1, -beta, -max([alpha, best_score]))
            cur_score = -cur_score
            if cur_score > best_score:
                best_score = cur_score
                best_move = move
                if best_score >= beta:
                    return [best_move, best_score]
        return [best_move, best_score]

class MonteCarlo(Player):
    
    def __init__(self, uf):
        self.uf = uf
        self.rp = RandomPlayer()

    def __str__(self):
        return 'Monte Carlo'

    def move(self, game, time_due):
        outcomes = [0] * game.num_moves()
        while time() < time_due:
            for move in range(0, len(outcomes)):
                new_game = game.copy()
                new_game.move(move)
                while not new_game.is_over():
                    new_game.move(self.rp.move(new_game, time_due))
                outcomes[move] += self.uf.eval(new_game, game.cur_player())
        return max(enumerate(outcomes), key=operator.itemgetter(1))[0]
