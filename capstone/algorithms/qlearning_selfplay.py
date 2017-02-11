from . import QLearning


class QLearningSelfPlay(QLearning):

    '''
    An specialization of the Q-learning algorithm that assumes
    a Game environment. In standard Q-learning the best action
    is the one that leads the the maximum reward. In this version
    we maximize for the first player of the game, and minimize
    for the second player.
    '''

    def max_qvalue(self):
        self._best = max if self.env.cur_state().cur_player() == 0 else min
        return super(QLearningSelfPlay, self).max_qvalue()
