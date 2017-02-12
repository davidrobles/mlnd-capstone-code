from . import QLearning
from .util import max_action_value, min_action_value


class QLearningSelfPlay(QLearning):

    '''
    An specialization of the Q-learning algorithm that assumes
    a Game environment. In standard Q-learning the best action
    is the one that selects the maximum reward. In this version
    we maximize for the first player of the game, and minimize
    for the second player.
    '''

    def best_action_value(self, qf, state, actions):
        if state.cur_player() == 0:
            return max_action_value(qf, state, actions)
        return min_action_value(qf, state, actions)
