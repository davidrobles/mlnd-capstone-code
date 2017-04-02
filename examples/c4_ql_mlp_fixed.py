'''
The Q-learning algorithm is used to learn a function approximator
for the state-action values of Connect-4 positions.
'''
from capstone.game.games import Connect4, TicTacToe
from capstone.game.players import RandPlayer
from capstone.rl import Environment, GameMDP, FixedGameMDP
from capstone.rl.learners import ApproximateQLearning
from capstone.rl.policies import EGreedy, RandomPolicy
from capstone.rl.utils import EpisodicWLDPlotter, Callback, LinearAnnealing
from capstone.rl.value_functions import MLP, QNetwork

# game = Connect4()
game = TicTacToe()
# mdp = GameMDP(game)
mdp = FixedGameMDP(game, RandPlayer(), 1)
env = Environment(mdp)
# qnetwork = QNetwork(n_input_units=42, n_output_units=7)
qnetwork = QNetwork(n_input_units=9, n_hidden_layers=3, n_output_units=9, n_hidden_units=100)
# qnetwork = QNetwork(n_input_units=42, n_hidden_layers=3, n_output_units=7, n_hidden_units=100)
egreedy = EGreedy(env.actions, qnetwork, 1.0)
qlearning = ApproximateQLearning(
    env=env,
    qfunction=qnetwork,
    policy=EGreedy(env.actions, qnetwork, 0.3),
    discount_factor=0.99, # change this to 1, and say because is deterministic
    n_episodes=100000,
    experience_replay=False
)
qlearning.train(
    callbacks=[
        EpisodicWLDPlotter(
            game=game,
            opp_player=RandPlayer(),
            n_matches=500,
            period=1000,
            filepath='figures/c4_ql_mlp_fixed.pdf'
        ),
        LinearAnnealing(egreedy, 'epsilon', init=1.0, final=0.1, n_episodes=50000)
    ]
)
