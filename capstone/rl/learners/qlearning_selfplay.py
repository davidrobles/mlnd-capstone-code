from .qlearning import QLearning
from ..util import max_qvalue, min_qvalue


class QLearningSelfPlay(QLearning):

    '''
    An specialization of the Q-learning algorithm that assumes
    a Game environment. In standard Q-learning the best action
    is the one that selects the maximum reward. In this version
    we maximize for the first player of the game, and minimize
    for the second player.
    '''

    def best_qvalue(self, state):
        best = max_qvalue if state.cur_player() == 0 else min_qvalue
        return best(state, self.env.actions(state), self.qf)
