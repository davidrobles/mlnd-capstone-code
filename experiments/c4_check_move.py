from keras.models import load_model
from capstone.game.games import Connect4 as C4
from capstone.game.players import AlphaBeta, GreedyQ, RandPlayer
from capstone.rl.value_functions import QNetwork
from capstone.game.utils import play_match

board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], # 6
         [' ', ' ', ' ', ' ', ' ', ' ', ' '], # 5
         [' ', ' ', ' ', ' ', ' ', ' ', ' '], # 4
         [' ', ' ', ' ', ' ', ' ', ' ', ' '], # 3
         [' ', ' ', ' ', ' ', ' ', ' ', ' '], # 2
         [' ', 'X', 'X', 'X', 'O', 'O', 'O']] # 1

move_mapper = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6}
qnetwork = QNetwork(move_mapper, None, None, None)
model = load_model('models/episode-52500-winpct-0.938')
c4 = C4(board)
# results = play_series(
#     game=c4,
#     players=[GreedyQ(mlp), RandPlayer()],
#     n_matches=100,
#     verbose=True
# )

def yeah(game, player):
    if game.is_over():
        utilities = {'W': 1.0, 'L': -1.0, 'D': 0.0}
        outcome = game.outcome(player)
        return utilities[outcome]
    best_func = max if player == 0 else min
    # game_moves = [(game, move) for move in game.legal_moves()]
    # _, best_score = best_func(game_moves, key=lambda gm: qnetwork[gm])
    return qnetwork[game]

players=[AlphaBeta(eval_func=yeah, max_depth=2), RandPlayer()]
play_match(c4, players)
