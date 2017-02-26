from __future__ import division
'''
The Q-learning algorithm is used to learn the state-action values for all
Tic-Tac-Toe positions by playing games against itself (self-play).
'''
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from capstone.game.games import TicTacToe
from capstone.game.players import GreedyQ, RandPlayer
from capstone.game.utils import play_series, tic2pdf
from capstone.rl import Environment, GameMDP
from capstone.rl.learners import QLearningSelfPlay
from capstone.rl.policies import EGreedy, RandomPolicy
from capstone.rl.utils import Callback
from capstone.rl.value_functions import TabularQ


class Plotter(Callback):

    def __init__(self, opp_player=RandPlayer(), n_episodes=10,
                 n_matches=1000, period=1, filename='test.pdf'):
        self.opp_player = opp_player
        self.n_matches = n_matches
        self.n_episodes = n_episodes
        self.period = period
        self.filename = filename
        self.x = []
        self.y_wins = []
        self.y_draws = []
        self.y_losses = []

    def on_episode_end(self, episode, qf):
        if (episode != (self.n_episodes - 1)) and episode % self.period != 0:
            return
        players = [GreedyQ(qf), self.opp_player]
        results = play_series(TicTacToe(), players, n_matches=self.n_matches, verbose=0)
        self.x.append(episode)
        self.y_wins.append(results['W'] / self.n_matches)
        self.y_draws.append(results['D'] / self.n_matches)
        self.y_losses.append(results['L'] / self.n_matches)

    def on_train_end(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        w_line, = ax.plot(self.x, self.y_wins, label='Win')
        l_line, = ax.plot(self.x, self.y_losses, label='Loss')
        d_line, = ax.plot(self.x, self.y_draws, label='Draw')
        ax.set_xlim([0, self.n_episodes])
        ax.set_ylim([0, 1.0])
        plt.xlabel('Episodes')
        formatter = FuncFormatter(lambda y, pos: '{}%'.format(y * 100))
        plt.gca().yaxis.set_major_formatter(formatter)
        plt.legend(handles=[w_line, l_line, d_line], loc=7)
        plt.savefig(self.filename)

n_episodes = 60000
plotter = Plotter(
    opp_player=RandPlayer(),
    n_episodes=n_episodes,
    n_matches=2000,
    period=1000,
    filename='tic_ql_tabular_selfplay_all.pdf'
)

game = TicTacToe()
env = Environment(GameMDP(game))
tabularq = TabularQ(random_state=23)
egreedy = EGreedy(env.actions, tabularq, epsilon=0.5, random_state=23)
rand_policy = RandomPolicy(env.actions, random_state=23)
qlearning = QLearningSelfPlay(
    env=env,
    qf=tabularq,
    policy=rand_policy,
    learning_rate=0.1,
    discount_factor=0.99,
    n_episodes=n_episodes,
    verbose=0,
    callbacks=[plotter]
)
qlearning.learn()
