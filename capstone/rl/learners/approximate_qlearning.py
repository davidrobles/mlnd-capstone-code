from ..learner import Learner
from ..policies import RandomPolicy
from ..util import max_qvalue
from ...utils import check_random_state


class ApproximateQLearning(Learner):

    def __init__(self, env, qf, policy=None, discount_factor=0.99, n_episodes=1000,
                 random_state=None, verbose=True):
        super(ApproximateQLearning, self).__init__(env, n_episodes=n_episodes, verbose=verbose)
        self.discount_factor = discount_factor
        self.random_state = check_random_state(random_state)
        self.policy = policy or RandomPolicy(env.actions, random_state=self.random_state)
        self.qf = qf

    def best_qvalue(self, state, actions):
        return max_qvalue(state, actions, self.qf)

    ###########
    # Learner #
    ###########

    def episode(self):
        while not self.env.is_terminal():
            state = self.env.cur_state()
            action = self.policy.action(state)
            reward, next_state = self.env.do_action(action)
            next_actions = self.env.actions(next_state)
            best_qvalue = self.best_qvalue(next_state, next_actions)
            update = reward + (self.discount_factor * best_qvalue)
            self.qf.update(state, update)
