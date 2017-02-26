'''
The Q-learning algorithm is used to learn the state-action values for all
Tic-Tac-Toe positions by playing games against itself (self-play).
'''
from capstone.game.games import TicTacToe
from capstone.game.players import RandPlayer
from capstone.rl import Environment, GameMDP
from capstone.rl.learners import QLearningSelfPlay
from capstone.rl.policies import EGreedy, RandomPolicy
from capstone.rl.utils import EpisodicWLDPlotter
from capstone.rl.value_functions import TabularQ

seed = 23
game = TicTacToe()
env = Environment(GameMDP(game))
tabularq = TabularQ(random_state=seed)
egreedy = EGreedy(env.actions, tabularq, epsilon=0.5, random_state=seed)
rand_policy = RandomPolicy(env.actions, random_state=seed)
qlearning = QLearningSelfPlay(
    env=env,
    qfunction=tabularq,
    policy=rand_policy,
    learning_rate=0.1,
    discount_factor=0.99,
    n_episodes=65000,
    callbacks=[
        EpisodicWLDPlotter(
            game=game,
            opp_player=RandPlayer(random_state=seed),
            n_matches=2000,
            period=1000,
            filename='figures/tic_ql_tabular_selfplay_all.pdf'
        )
    ]
)
qlearning.learn()
