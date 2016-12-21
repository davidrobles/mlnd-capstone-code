'''Implements TD(0) to learn a value function for Tic Tac Toe
'''
import random
from capstone.game import TicTacToe
from capstone.player import RandPlayer
from capstone.util import play_series, ZobristHashing


class TD0(object):

    def __init__(self, game, eval_func, n_episodes, alpha, gamma, epsilon):
        self.cur_episode = 0
        self.game = game
        self.eval_func = eval_func
        self.n_episodes = n_episodes
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def learn(self):
        for episode in self.n_episodes:
            self.game.reset()
            while self.game.is_over():
                prev = game.copy()
                self.game.make_move()
                cur = self.eval_func(prev, 0)
                nxt = self.eval_func(game, 0)
                td_error = self.alpha * (self.gamma * nxt - cur) * (1 - cur * cur)
                self.eval_func
