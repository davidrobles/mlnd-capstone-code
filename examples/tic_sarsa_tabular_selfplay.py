'''
Sarsa with self-play is used to learn the state-action values
for all Tic-Tac-Toe board positions.
'''
from capstone.game.games import TicTacToe
from capstone.game.players import RandPlayer
from capstone.rl import FixedGameMDP, Environment
from capstone.rl.learners import SarsaSelfPlay
from capstone.rl.policies import RandomPolicy
from capstone.rl.value_functions import TabularQ
from capstone.rl.utils import EpisodicWLDPlotter

seed = 23
game = TicTacToe()
mdp = FixedGameMDP(game, RandPlayer(random_state=seed), 1)
env = Environment(mdp)
sarsa = SarsaSelfPlay(
    env=env,
    qfunction=TabularQ(random_state=seed),
    policy=RandomPolicy(env.actions, random_state=seed),
    learning_rate=0.1,
    discount_factor=0.99,
    n_episodes=60000
)
sarsa.learn(
    callbacks=[
        EpisodicWLDPlotter(
            game=game,
            opp_player=RandPlayer(random_state=seed),
            n_matches=2000,
            period=1000,
            filepath='figures/tic_sarsa_tabular_selfplay.pdf'
        )
    ]
)
