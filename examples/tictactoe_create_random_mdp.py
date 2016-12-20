'''Randomly creates a player that makes the same move in a given board position.
'''
from copy import copy
import random
from capstone.game import TicTacToe
from capstone.player import RandPlayer
from capstone.util import play_series, ZobristHashing

zobrist_hash = ZobristHashing(n_positions=9, n_pieces=2)

def count_positions(game, hashed_boards):
    board_hash = zobrist_hash(game.board)
    if board_hash not in hashed_boards:
        if game.is_over():
            hashed_boards[board_hash] = None
        else:
            hashed_boards[board_hash] = random.choice(game.legal_moves())
    for move in game.legal_moves():
        new_game = copy(game)
        new_game.make_move(move)
        count_positions(new_game, hashed_boards)

game = TicTacToe()
hashed_boards = {}
count_positions(copy(game), hashed_boards)

class NewPlayer(object):

    def __init__(self, table):
        self.table = table

    def choose_move(self, game):
        return self.table[zobrist_hash(game.board)]

players = [RandPlayer(), NewPlayer(hashed_boards)]
play_series(game, players)
