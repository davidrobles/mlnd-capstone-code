'''
The Q-learning algorithm is used to learn the state-action values for all
Tic-Tac-Toe positions by playing games against itself (self-play).
'''
from capstone.game.games import TicTacToe
from capstone.game.players import RandPlayer
from capstone.rl import Environment, GameMDP
from capstone.rl.learners import ApproxQLearningSelfPlay
from capstone.rl.policies import RandomPolicy
from capstone.rl.utils import EpisodicWLDPlotter
from capstone.rl.value_functions import MLP

seed = 23
game = TicTacToe()
mdp = GameMDP(game)
env = Environment(mdp)
mlp = MLP()
qlearning = ApproxQLearningSelfPlay(
    env=env,
    qfunction=MLP(),
    policy=RandomPolicy(env.actions, random_state=seed),
    discount_factor=0.99,
    n_episodes=100000,
    callbacks=[
        EpisodicWLDPlotter(
            game=game,
            opp_player=RandPlayer(random_state=seed),
            n_matches=100,
            period=1000,
            filepath='figures/tic_ql_mlp_selfplay_all.pdf'
        )
    ]
)
qlearning.train()
