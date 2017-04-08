# -*- coding: utf-8 -*-
'''
Use the Q-learning algorithm to train a neural network
function approximator to play Connect 4.

This example worked very well, it achieved a win % of ~97%, with a loss % of ~3%.
'''
from capstone.game.games import Connect4
from capstone.game.players import RandPlayer
from capstone.rl import Environment, GameMDP, FixedGameMDP
from capstone.rl.learners import ApproximateQLearning
from capstone.rl.policies import EGreedy
from capstone.rl.utils import EpisodicWLDPlotter, Callback, LinearAnnealing
from capstone.rl.value_functions import QNetwork

move_mapper = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6}

board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', 'O', ' ', 'O', ' '],
         [' ', ' ', 'O', 'X', ' ', 'X', ' '],
         [' ', ' ', 'X', 'O', ' ', 'X', ' '],
         [' ', 'O', 'O', 'X', 'X', 'X', 'O']]
game = Connect4(board)
mdp = GameMDP(game)
# mdp = FixedGameMDP(game, RandPlayer(), 1)
env = Environment(mdp)
qnetwork = QNetwork(
    move_mapper,
    n_input_units=42,
    n_hidden_layers=1,
    n_output_units=7,
    n_hidden_units=100
)
egreedy = EGreedy(
    provider=env.actions,
    qfunction=qnetwork,
    epsilon=1.0,
    selfplay=True
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

class Hey(Callback):
    def on_episode_begin(self, episode, qfunction):
        import keras
        if episode % 50 == 0:
            print('Episode {}'.format(episode))
            print(' * ε = {}'.format(egreedy.epsilon))
            print(' * lr = {}'.format(keras.backend.get_value(qnetwork.model.optimizer.lr)))
            # lr = self.model.optimizer.lr.get_value()
            # self.model.optimizer.lr.set_value(lr*self.reduce_rate)

qlearning.train(
    n_episodes=20000,
    callbacks=[
        EpisodicWLDPlotter(
            game=game,
            opp_player=RandPlayer(),
            n_matches=1000,
            period=250,
            filepath='figures/c4_ql_fa_selfplay.pdf'
        ),
        # LinearAnnealing(egreedy, 'epsilon', init=1.0, final=0.1, n_episodes=10000),
        Hey()
    ]
)

# be careful with the testing of players

# decrease learning rate

# try rmsprop

# use replay_start_size
