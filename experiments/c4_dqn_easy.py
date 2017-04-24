# -*- coding: utf-8 -*-
'''
Use Q-learning with a Deep Q-Network as a function approximator
to learn to play a simple position of Connect 4 in which the player
in turn has a guaranteed win. The idea of this experiment is to verify
that our implementation of ApproximateQLearning, selfplay, and 
experience replay are working correctly.
'''
from capstone.game.games import Connect4
from capstone.game.players import RandPlayer
from capstone.game.utils import c42pdf
from capstone.rl import Environment, GameMDP, FixedGameMDP
from capstone.rl.learners import ApproximateQLearning
from capstone.rl.policies import EGreedy
from capstone.rl.utils import EpisodicWLDPlotter, Callback, LinearAnnealing
from capstone.rl.value_functions import QNetwork
import numpy as np
import random

seed = 48
random.seed(seed)
np.random.seed(seed)

move_mapper = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6}

# The Complete Book of Connect 4 
# Problem Set A (Easy)
# Problem 1, Page 16
# Red wins with C4
#         A    B    C    D    E    F    G
board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], # 6
         [' ', ' ', ' ', ' ', ' ', ' ', ' '], # 5
         [' ', ' ', ' ', 'O', ' ', 'O', ' '], # 4
         [' ', ' ', 'O', 'X', ' ', 'X', ' '], # 3
         [' ', ' ', 'X', 'O', ' ', 'X', ' '], # 2
         [' ', 'O', 'O', 'X', 'X', 'X', 'O']] # 1

c42pdf('figures/c4_dqn_easy_board.pdf', board)
game = Connect4(board)
mdp = GameMDP(game)
env = Environment(mdp)
qnetwork = QNetwork(
    move_mapper,
    n_input_units=42,
    n_hidden_layers=2,
    n_output_units=7,
    n_hidden_units=100,
    learning_rate=0.01
)
egreedy = EGreedy(
    provider=env.actions,
    qfunction=qnetwork,
    epsilon=1.0,
    selfplay=True,
    random_state=seed
)
qlearning = ApproximateQLearning(
    env=env,
    qfunction=qnetwork,
    policy=egreedy,
    discount_factor=0.99,
    selfplay=True,
    experience_replay=True,
    replay_memory_size=10000,
    batch_size=32
)
class Monitor(Callback):
    def on_episode_begin(self, episode, qfunction):
        if episode % 50 == 0:
            print('Episode {}'.format(episode))
qlearning.train(
    n_episodes=1200,
    callbacks=[
        EpisodicWLDPlotter(
            game=game,
            opp_player=RandPlayer(random_state=seed),
            n_matches=1000,
            period=25,
            filepath='figures/c4_dqn_easy_plot.pdf'
        ),
        LinearAnnealing(egreedy, 'epsilon', init=1.0, final=0.1, n_episodes=1000),
        Monitor()
    ]
)

from capstone.game.players import GreedyQ
g = GreedyQ(qnetwork)
print 'Move:', g.choose_move(game)

# IMPORTANT: dont forget to filter the best value, ignore the ilegal moves
