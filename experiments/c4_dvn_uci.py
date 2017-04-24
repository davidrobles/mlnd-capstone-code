import pandas as pd
from capstone.datasets.ucic4 import get_random_game, get_random_win_game, \
                                    get_random_draw_game, get_random_loss_game
from capstone.game.games import Connect4 as C4
from capstone.game.players import RandPlayer
from capstone.rl import Environment, GameMDP, FixedGameMDP
from capstone.rl.learners import ApproximateQLearning as ApproxQLearning
from capstone.rl.policies import EGreedy, RandomPolicy
from capstone.rl.utils import EpisodicWLDPlotter, Callback, LinearAnnealing
from capstone.rl.value_functions.c4deepnetwork import Connect4DeepNetwork
import numpy as np
import random

seed = 383
random.seed(seed)
np.random.seed(seed)

mdp = FixedGameMDP(get_random_game(), RandPlayer(random_state=seed), 1)
env = Environment(mdp)
c4dn = Connect4DeepNetwork()
egreedy = EGreedy(action_space=env.actions, qfunction=c4dn, epsilon=1.0,
                  selfplay=False, random_state=seed)
qlearning = ApproxQLearning(env=env, qfunction=c4dn, policy=egreedy,
                            discount_factor=0.99, selfplay=False,
                            experience_replay=True, replay_memory_size=20000,
                            batch_size=32)

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

period = 500
n_matches = 1000

qlearning.train(
    n_episodes=15000,
    callbacks=[
        EpisodicWLDPlotter(
            game=get_random_win_game,
            opp_player=RandPlayer(random_state=seed),
            n_matches=n_matches,
            period=period,
            filepath='figures/c4dn_uci_wins.pdf'
        ),
        EpisodicWLDPlotter(
            game=get_random_draw_game,
            opp_player=RandPlayer(random_state=seed),
            n_matches=n_matches,
            period=period,
            filepath='figures/c4dn_uci_draws.pdf'
        ),
        EpisodicWLDPlotter(
            game=get_random_loss_game,
            opp_player=RandPlayer(random_state=seed),
            n_matches=n_matches,
            period=period,
            filepath='figures/c4dn_uci_losses.pdf'
        ),
        LinearAnnealing(egreedy, 'epsilon', init=1.0, final=0.1, n_episodes=5000),
        Monitor()
    ]
)

# re run experiment with wins to use get_random_game

# consolidate experiment in one file
