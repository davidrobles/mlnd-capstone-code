from capstone.game.games import TicTacToe
from capstone.game.players import AlphaBeta
from capstone.game.utils import tic2pdf
from capstone.rl import GameMDP
from capstone.rl.learners import MinimaxQ
from capstone.rl.policies import RandomPolicy, EGreedy
from capstone.rl.utils import Experience
from capstone.rl.value_functions import TabularVF
from capstone.rl.mdp import AlternatingMarkovGame


board = [[' ', ' ', 'X'],
         [' ', 'X', ' '],
         ['O', 'O', ' ']]

amg = AlternatingMarkovGame(TicTacToe(board))

minimaxq = MinimaxQ(
    action_space=amg.actions,
    qfunction=TabularVF(),
    policy=RandomPolicy(action_space=amg.actions),
    learning_rate=0.1,
    discount_factor=1.0
)

policies = [minimaxq, minimaxq]

class MDPTrainer(object):

    def __init__(self, game, policy):
        self.game = game
        self.policy = policy


class SAMTrainer(object):
    '''
    # Arguments
        amg: an alternating markov game.
        policies: a list of two policies.
    '''

    def __init__(self, amg, policies):
        self.amg = amg
        self.policies = policies

    def train(self, n_episodes, callbacks=None):
        for episode in range(n_episodes):
            print('Episode {}'.format(episode))
            state = self.amg.start_state()
            while not self.amg.is_terminal(state):
                cur_player = self.amg.cur_player(state)
                policy = self.policies[cur_player]
                action = policy.get_action(state)
                for ns, prob in self.amg.transitions(state, action):
                    next_state = ns
                reward = self.amg.reward(state, action, next_state)
                done = self.amg.is_terminal(next_state)
                if hasattr(policy, 'update'):
                    experience = Experience(state, action, reward, next_state, done)
                    policy.update(experience, max if next_state.cur_player() == 0 else min)
                state = next_state

trainer = SAMTrainer(amg, policies)
trainer.train(5000)

game = TicTacToe(board)
for move in game.legal_moves():
    print('*' * 80)
    value = minimaxq.qfunction[game, move]
    print('Move: %d' % move)
    print('Value: %f' % value)
    new_game = game.copy().make_move(move)
    print(new_game)
    filename = 'figures/tic_ql_tab_move_{}.pdf'.format(move)
    tic2pdf(filename, new_game.board)
