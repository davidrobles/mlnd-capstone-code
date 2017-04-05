'''
Use the Q-learning algorithm to train a neural network
function approximator to play Connect 4.

This example worked very well, it achieved a win % of ~97%, with a loss % of ~3%.
'''
from capstone.game.games import Connect4
from capstone.game.players import RandPlayer
from capstone.rl import Environment, GameMDP, FixedGameMDP
from capstone.rl.learners import ApproximateQLearningSelfPlay, ApproximateQLearning
from capstone.rl.policies import EGreedy
from capstone.rl.utils import EpisodicWLDPlotter, Callback, LinearAnnealing
from capstone.rl.value_functions import QNetwork

move_mapper = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6}

board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', 'O', ' ', 'O', ' '],
         [' ', ' ', 'O', 'X', ' ', 'X', ' '],
         [' ', ' ', 'X', 'O', ' ', 'X', ' '],
         [' ', 'O', 'O', 'X', 'X', 'X', 'O']]
game = Connect4(board)
# mdp = GameMDP(game)
mdp = FixedGameMDP(game, RandPlayer(), 1)
env = Environment(mdp)
qnetwork = QNetwork(
    move_mapper,
    n_input_units=42,
    n_hidden_layers=1,
    n_output_units=7,
    n_hidden_units=100
)
egreedy = EGreedy(env.actions, qnetwork, 1.0)
qlearning = ApproximateQLearning(
    env=env,
    qfunction=qnetwork,
    policy=egreedy,
    discount_factor=1.0,
    n_episodes=30000,
    experience_replay=True,
    replay_memory_size=10000,
    batch_size=32
)
qlearning.train(
    callbacks=[
        EpisodicWLDPlotter(
            game=game,
            opp_player=RandPlayer(),
            n_matches=1000,
            period=500,
            filepath='figures/c4_ql_fa.pdf'
        ),
        LinearAnnealing(egreedy, 'epsilon', init=1.0, final=0.1, n_episodes=15000)
    ]
)
