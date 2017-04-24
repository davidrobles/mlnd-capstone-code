from capstone.game.games import TicTacToe
from capstone.game.players import RandPlayer
from capstone.rl import GameMDP, FixedGameMDP, Environment
from capstone.rl.learners import ApproximateQLearning
from capstone.rl.policies import RandomPolicy
from capstone.rl.utils import EpisodicWLDPlotter, QValuesPlotter
from capstone.rl.value_functions import MLP

seed = 23
game = TicTacToe()
env = Environment(FixedGameMDP(game, RandPlayer(), 1))
mlp = MLP()
qlearning = ApproximateQLearning(
    env=env,
    policy=RandomPolicy(env.actions, random_state=seed),
    qfunction=mlp,
    discount_factor=1.0,
    n_episodes=50000
)
qlearning.train(
    callbacks=[
        EpisodicWLDPlotter(
            game=game,
            opp_player=RandPlayer(random_state=seed),
            n_matches=1000,
            period=5000,
            # filepath='../mlnd-capstone-report/figures/tic_ql_tab_full_selfplay_wld_plot.pdf'
            filepath='figures/test88.pdf'
        )
    ]
)
# mlp.model.save('models/qltic.h5')
