from __future__ import division
'''
The Q-learning algorithm is used to learn the state-action values for all
Tic-Tac-Toe positions by playing games against itself (self-play).
'''
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from capstone.game.games import TicTacToe
from capstone.game.players import GreedyQ, RandPlayer
from capstone.game.utils import play_series, tic2pdf
from capstone.rl import Environment, GameMDP
from capstone.rl.learners import QLearningSelfPlay
from capstone.rl.policies import RandomPolicy
from capstone.rl.utils import Callback

n_episodes = 60000

game = TicTacToe()
env = Environment(GameMDP(game))

class My(Callback):

    def __init__(self):
        self.x = []
        self.y_wins = []
        self.y_draws = []
        self.y_losses = []

    def on_episode_end(self, episode, qf):
        if episode % 1000 == 0:
            players = [GreedyQ(qf), RandPlayer()]
            n_matches = 1000
            results = play_series(TicTacToe(), players, n_matches=n_matches, verbose=0)
            self.x.append(episode)
            win_pct = results['W'] / n_matches
            self.y_wins.append(win_pct)
            draw_pct = results['D'] / n_matches
            self.y_draws.append(draw_pct)
            loss_pct = results['L'] / n_matches
            self.y_losses.append(loss_pct)

    def on_train_end(self):
        x = np.array(self.x)
        y_wins = np.array(self.y_wins)
        y_draws = np.array(self.y_draws)
        y_losses = np.array(self.y_losses)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        w_line, = ax.plot(x, y_wins, label='Win %')
        d_line, = ax.plot(x, y_draws, label='Draw %')
        l_line, = ax.plot(x, y_losses, label='Loss %')
        ax.set_xlim([0, n_episodes])
        ax.set_ylim([0, 1.0])
        plt.xlabel('Episodes')
        plt.ylabel('Pct')
        plt.legend(handles=[w_line, d_line, l_line])
        plt.savefig('hey45.pdf')


qlearning = QLearningSelfPlay(env, policy=RandomPolicy(env.actions), learning_rate=0.1,
                              discount_factor=0.99, n_episodes=n_episodes, verbose=0,
                              callbacks=[My()])
qlearning.learn()
