import pandas as pd
from capstone.datasets.ucic4 import get_random_game, get_random_win_game
from capstone.game.games import Connect4 as C4
from capstone.game.players import RandPlayer
from capstone.rl import Environment, GameMDP, FixedGameMDP
from capstone.rl.learners import ApproximateQLearning
from capstone.rl.policies import EGreedy, RandomPolicy
from capstone.rl.utils import EpisodicWLDPlotter, Callback, LinearAnnealing
from capstone.rl.value_functions import QNetwork
import numpy as np
import random

move_mapper = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6}

seed = 84
random.seed(seed)
np.random.seed(seed)


mdp = FixedGameMDP(get_random_game(), RandPlayer(random_state=seed), 1)
env = Environment(mdp)
qnetwork = QNetwork(
    move_mapper,
    n_input_units=42,
    n_hidden_layers=3,
    n_output_units=7,
    n_hidden_units=400,
    learning_rate = 0.001
)
egreedy = EGreedy(
    action_space=env.actions,
    qfunction=qnetwork,
    epsilon=1.0,
    selfplay=False,
    random_state=seed
)
qlearning = ApproximateQLearning(
    env=env,
    qfunction=qnetwork,
    policy=egreedy,
    discount_factor=0.99,
    selfplay=False,
    experience_replay=True,
    replay_memory_size=1000,
    batch_size=32
)
class Monitor(Callback):
    def on_episode_begin(self, episode, qfunction):
        mdp = FixedGameMDP(get_random_game(), RandPlayer(random_state=seed), 1)
        env = Environment(mdp)
        qlearning.env = env
        egreedy.action_space = env.actions
        qlearning.policy.provider = env.actions
        if episode % 50 == 0:
            print('Episode {}'.format(episode))

# prepopulate replay memory? read deepmind paper

qlearning.train(
    n_episodes=100000,
    callbacks=[
        EpisodicWLDPlotter(
            game=get_random_win_game,
            opp_player=RandPlayer(random_state=seed),
            n_matches=1000,
            period=500,
            filepath='figures/c4_dqn_uci.pdf'
        ),
        LinearAnnealing(egreedy, 'epsilon', init=1.0, final=0.1, n_episodes=10000),
        Monitor()
    ]
)

# got 90% with 42 input units, 3 hidden layers, 7 output units, 400 hidden units, lr=0.001, no
# selfplay, only a 1,000 experience replay size, 100000 episodes, and linear annealing for 10,000
# episodes only
