'''
Q-Learning is used to estimate the state-action values for all
Tic-Tac-Toe positions by playing games against itself (self-play).
'''
from capstone.game.games import TicTacToe
from capstone.game.players import RandPlayer
from capstone.game.utils import tic2pdf
from capstone.rl import Environment, GameMDP
from capstone.rl.learners import QLearning
from capstone.rl.policies import RandomPolicy
from capstone.rl.utils import EpisodicWLDPlotter
from capstone.rl.value_functions import TabularVF

seed = 23
game = TicTacToe()
mdp = GameMDP(game)
env = Environment(mdp)
qlearning = QLearning(
    env=env,
    qfunction=TabularVF(random_state=seed),
    policy=RandomPolicy(action_space=env.action_space, random_state=seed),
    learning_rate=0.1,
    discount_factor=1.0,
    selfplay=True
)
qlearning.train(
    n_episodes=70000,
    callbacks=[
        EpisodicWLDPlotter(
            game=game,
            opp_player=RandPlayer(random_state=seed),
            n_matches=1000,
            period=1000,
            filepath='../mlnd-capstone-report/figures/tic_ql_tab_full_selfplay_wld_plot.pdf'
        )
    ]
)
