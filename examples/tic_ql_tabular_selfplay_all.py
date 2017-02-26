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
from capstone.rl.policies import RandomPolicy
from capstone.rl.utils import Callback

n_episodes = 100000
game = TicTacToe()
env = Environment(GameMDP(game))

class Plotter(Callback):

    def __init__(self):
        self.x = []
        self.y_wins = []
        self.y_draws = []
        self.y_losses = []

    def on_episode_end(self, episode, qf):
        if (episode != (n_episodes - 1)) and episode % 1000 != 0:
            return
        players = [GreedyQ(qf), RandPlayer()]
        n_matches = 1000
        results = play_series(TicTacToe(), players, n_matches=n_matches, verbose=0)
        self.x.append(episode)
        self.y_wins.append(results['W'] / n_matches)
        self.y_draws.append(results['D'] / n_matches)
        self.y_losses.append(results['L'] / n_matches)

    def on_train_end(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        w_line, = ax.plot(self.x, self.y_wins, label='Win')
        d_line, = ax.plot(self.x, self.y_draws, label='Draw')
        l_line, = ax.plot(self.x, self.y_losses, label='Loss')
        ax.set_xlim([0, n_episodes])
        ax.set_ylim([0, 1.0])
        plt.xlabel('Episodes')
        formatter = FuncFormatter(lambda y, pos: '{}%'.format(y * 100))
        plt.gca().yaxis.set_major_formatter(formatter)
        plt.legend(handles=[w_line, d_line, l_line])
        plt.savefig('tic_ql_tabular_selfplay_all.pdf')

behavior_policy = RandomPolicy(env.actions, random_state=23)
qlearning = QLearningSelfPlay(env, policy=behavior_policy, learning_rate=0.1,
                              discount_factor=0.99, n_episodes=n_episodes, verbose=0,
                              callbacks=[Plotter()])
qlearning.learn()
