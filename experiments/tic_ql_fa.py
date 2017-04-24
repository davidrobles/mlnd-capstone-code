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

mapping = { int(x): int(x) - 1 for x in range(1, 10)}

game = TicTacToe()
# mdp = GameMDP(game)
mdp = FixedGameMDP(game, RandPlayer(), 1)
env = Environment(mdp)
qnetwork = QNetwork(mapping, n_input_units=9, n_hidden_layers=1, n_output_units=9, n_hidden_units=100)
egreedy = EGreedy(env.actions, qnetwork, 1.0)
qlearning = ApproximateQLearning(
    env=env,
    qfunction=qnetwork,
    policy=egreedy,
    discount_factor=1.0,
    experience_replay=True,
    batch_size=32
)
qlearning.train(
    n_episodes=10000,
    callbacks=[
        EpisodicWLDPlotter(
            game=game,
            opp_player=RandPlayer(),
            n_matches=1000,
            period=250,
            filepath='figures/tic_deep_ql.pdf'
        ),
        LinearAnnealing(egreedy, 'epsilon', init=1.0, final=0.1, n_episodes=5000)
    ]
)

# n_episodes = 4,000
# n_episodes_annearling = 2,000

# mention that I tried adam and rmsprop but they did not work
