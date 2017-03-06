'''
The Q-learning algorithm is used to learn a function approximator
for the state-action values of Connect-4 positions.
'''
from capstone.game.games import Connect4
from capstone.game.players import RandPlayer
from capstone.rl import Environment, FixedGameMDP
from capstone.rl.learners import ApproximateQLearning
from capstone.rl.policies import EGreedy, RandomPolicy
from capstone.rl.utils import EpisodicWLDPlotter
from capstone.rl.value_functions import MLP, DQN

board = [['X', 'O', 'O', ' ', 'O', ' ', ' '],
         ['X', 'O', 'X', ' ', 'X', ' ', ' '],
         ['O', 'X', 'O', 'X', 'O', 'X', 'O'],
         ['O', 'X', 'O', 'X', 'O', 'X', 'O'],
         ['X', 'O', 'X', 'O', 'X', 'O', 'X'],
         ['X', 'O', 'X', 'O', 'X', 'O', 'X']]
game = Connect4(board)
mdp = FixedGameMDP(game, RandPlayer(), 1)
env = Environment(mdp)
dqn = DQN()
qlearning = ApproximateQLearning(
    env=env,
    qfunction=dqn,
    policy=RandomPolicy(env.actions),
    # policy=EGreedy(env.actions, dqn, 0.3),
    discount_factor=1.0, # change this to 1, and say because is deterministic
    n_episodes=50000,
    experience_replay=True
)
qlearning.train(
    callbacks=[
        EpisodicWLDPlotter(
            game=game,
            opp_player=RandPlayer(),
            n_matches=1000,
            period=2000,
            filepath='figures/c4_ql_mlp_fixed.pdf'
        )
    ]
)

for move in game.legal_moves():
    print('*' * 80)
    next_game = game.copy().make_move(move)
    print('Move: %s' % move)
    print('Value: %f' % dqn[(next_game, move)])
    print(next_game)
    # filename = 'figures/c4_ql_move_%s_value_%.4f.pdf' % (move, value)
    # c42pdf(filename, new_game.board)
