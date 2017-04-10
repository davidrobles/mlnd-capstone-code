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

seed = 48
random.seed(seed)
np.random.seed(seed)


mdp = FixedGameMDP(get_random_game(), RandPlayer(random_state=seed), 1)
env = Environment(mdp)
qnetwork = QNetwork(
    move_mapper,
    n_input_units=42,
    n_hidden_layers=1,
    n_output_units=7,
    n_hidden_units=400,
    learning_rate=0.01
)
# egreedy = EGreedy(
#     action_space=env.actions,
#     qfunction=qnetwork,
#     epsilon=1.0,
#     selfplay=False,
#     random_state=seed
# )
qlearning = ApproximateQLearning(
    env=env,
    qfunction=qnetwork,
    # policy=egreedy,
    policy=RandomPolicy(env.actions, random_state=seed),
    discount_factor=0.99,
    selfplay=False,
    experience_replay=True,
    replay_memory_size=10000,
    batch_size=32
)
class Monitor(Callback):
    def on_episode_begin(self, episode, qfunction):
        mdp = FixedGameMDP(get_random_game(), RandPlayer(random_state=seed), 1)
        env = Environment(mdp)
        qlearning.env = env
        # egreedy.action_space = env.actions
        qlearning.policy.provider = env.actions
        if episode % 50 == 0:
            print('Episode {}'.format(episode))

def hey():
    qlearning.train(
        n_episodes=10000,
        callbacks=[
            EpisodicWLDPlotter(
                game=get_random_win_game,
                opp_player=RandPlayer(random_state=seed),
                n_matches=1000,
                period=250,
                filepath='figures/c4_dqn_uci.pdf'
            ),
            # LinearAnnealing(egreedy, 'epsilon', init=1.0, final=0.1, n_episodes=25000),
            Monitor()
        ]
    )

# import cProfile
# cProfile.run('hey()')
hey()
