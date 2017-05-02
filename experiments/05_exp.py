import numpy as np
from capstone.datasets.ucic4 import get_random_win_game, get_random_loss_game
from capstone.game.players.kerasplayer import KerasStatePlayer
from capstone.game.players import RandPlayer
from capstone.game.utils import play_match, play_series
from capstone.utils import print_aec, str_aec

keras = KerasStatePlayer('models/episode-14500-winpct-0.942')
rnd = RandPlayer()

N_EVALUATIONS = 100
N_MATCHES_PER_EVALUATION = 100


def run_evaluation(generator, players, expected):
    '''
    Returns the accuracy of the predition.
    '''
    print 'Running experiment for %s' % expected
    outcomes = []
    for i in range(N_EVALUATIONS):
        print 'Episode %d' % i
        results = play_series(
            game=generator(),
            players=players,
            n_matches=N_MATCHES_PER_EVALUATION,
            verbose=False
        )
        outcomes.append(results[expected] / float(N_MATCHES_PER_EVALUATION))
    return np.mean(outcomes)


print run_evaluation(
    generator=get_random_win_game,
    players = [keras, keras],
    # players = [rnd, rnd],
    expected='W'
)

# print run_evaluation(
#     generator=get_random_loss_game,
#     players = [keras, keras],
#     expected='L'
# )
