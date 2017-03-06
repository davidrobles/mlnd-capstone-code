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

    def __init__(self, game, opp_player, n_matches=1000, period=1, filepath='test.pdf'):
        self.game = game
        self.opp_player = opp_player
        self.n_matches = n_matches
        self.period = period
        self.filepath = filepath
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
        win_pct = (results['W'] / self.n_matches) * 100
        draw_pct = (results['D'] / self.n_matches) * 100
        loss_pct = (results['L'] / self.n_matches) * 100
        print('-  Win %: {}'.format(win_pct))
        print('-  Draw %: {}'.format(draw_pct))
        print('-  Loss %: {}'.format(loss_pct))
        self.y_wins.append(win_pct)
        self.y_draws.append(draw_pct)
        self.y_losses.append(loss_pct)

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
        formatter = FuncFormatter(lambda y, _: '{:d}%'.format(int(y * 100)))
        plt.gca().yaxis.set_major_formatter(formatter)
        plt.legend(handles=[w_line, l_line, d_line], loc=7)
        plt.savefig(self.filepath)


class QValuesPlotter(Callback):
    '''
    Plots the Q-values of the given state and actions during training.
    '''

    def __init__(self, state, actions):
        self.state = state
        self.actions = actions
        self.x = []
        self.y = [[] for _ in range(len(self.actions))]

    def on_episode_end(self, episode, qfunction):
        self.x.append(episode)
        for i, action in enumerate(self.actions):
            self.y[i].append(qfunction[self.state, action])

    def on_train_end(self, qf):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        lines = []
        for i, action in enumerate(self.actions):
            line, = ax.plot(self.x, self.y[i], label='Q(s,{})'.format(action))
            lines.append(line)
        ax.set_xlim([0, 800])
        ax.set_ylim([-1.0, 1.0])
        plt.xlabel('Episodes')
        plt.ylabel('Action Value (Q)')
        plt.legend(handles=lines, loc=7)
        plt.savefig('figures/robles.pdf')
