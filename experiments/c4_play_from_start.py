from keras.models import load_model
from capstone.game.games import Connect4
from capstone.game.players import AlphaBeta, GreedyQ, KerasPlayer, RandPlayer
from capstone.game.players.kerasplayer import KerasStatePlayer
from capstone.game.utils import play_match, play_series
from capstone.rl.value_functions import QNetwork

results = play_series(
    game=Connect4(),
    # players=[KerasStatePlayer('models/episode-14500-winpct-0.942'), RandPlayer()],
    players=[RandPlayer(), KerasStatePlayer('models/episode-14500-winpct-0.942')],
    # players=[RandPlayer(), RandPlayer()],
    n_matches=100,
    verbose=True
)
