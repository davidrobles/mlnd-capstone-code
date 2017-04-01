'''
The Q-learning algorithm is used to learn a function approximator
for the state-action values of Tic-Tac-Toe positions.
'''
from capstone.game.games import TicTacToe
from capstone.game.players import RandPlayer
from capstone.rl import Environment, GameMDP, FixedGameMDP
from capstone.rl.learners import ApproximateQLearning
from capstone.rl.policies import EGreedy
from capstone.rl.utils import EpisodicWLDPlotter, Callback, LinearAnnealing
from capstone.rl.value_functions import QNetwork

game = TicTacToe()
mdp = FixedGameMDP(game, RandPlayer(), 1)
env = Environment(mdp)
qnetwork = QNetwork(n_input_units=9, n_hidden_layers=3, n_output_units=9, n_hidden_units=100)
egreedy = EGreedy(env.actions, qnetwork, 1.0)
qlearning = ApproximateQLearning(
    env=env,
    qfunction=qnetwork,
    policy=egreedy,
    discount_factor=0.99,
    n_episodes=10000,
    experience_replay=False
)
qlearning.train(
    callbacks=[
        EpisodicWLDPlotter(
            game=game,
            opp_player=RandPlayer(),
            n_matches=500,
            period=1000,
            filepath='figures/tic_ql_qnetwork.pdf'
        ),
        LinearAnnealing(egreedy, 'epsilon', init=1.0, final=0.1, n_episodes=5000)
    ]
)
