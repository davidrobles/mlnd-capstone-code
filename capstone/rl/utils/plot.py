from __future__ import division
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from .callbacks import Callback
from ...game.players import GreedyQ, RandPlayer
from ...game.utils import play_series


class EpisodicWLDPlotter(Callback):
    '''
    Plots the episodic win, loss and draws of a learner
    against a fixed opponent
    '''

    def __init__(self, game, opp_player=RandPlayer(), n_matches=1000,
                 period=1, filename='test.pdf'):
        self.game = game
        self.opp_player = opp_player
        self.n_matches = n_matches
        self.period = period
        self.filename = filename
        self.x = []
        self.y_wins = []
        self.y_draws = []
        self.y_losses = []

    def on_episode_end(self, episode, qf):
        if episode % self.period != 0:
            return
        self._plot(episode, qf)

    def _plot(self, episode, qf):
        results = play_series(
            game=self.game.copy(),
            players=[GreedyQ(qf), self.opp_player],
            n_matches=self.n_matches,
            verbose=False
        )
        self.x.append(episode)
        self.y_wins.append(results['W'] / self.n_matches)
        self.y_draws.append(results['D'] / self.n_matches)
        self.y_losses.append(results['L'] / self.n_matches)

    def on_train_end(self, qf):
        n_episodes = len(self.x) * self.period
        self._plot(n_episodes - 1, qf)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        w_line, = ax.plot(self.x, self.y_wins, label='Win')
        l_line, = ax.plot(self.x, self.y_losses, label='Loss')
        d_line, = ax.plot(self.x, self.y_draws, label='Draw')
        ax.set_xlim([0, n_episodes])
        ax.set_ylim([0, 1.0])
        plt.xlabel('Episodes')
        formatter = FuncFormatter(lambda y, pos: '{}%'.format(y * 100))
        plt.gca().yaxis.set_major_formatter(formatter)
        plt.legend(handles=[w_line, l_line, d_line], loc=7)
        plt.savefig(self.filename)
