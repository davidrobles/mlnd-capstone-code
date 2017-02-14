import random
from .tabularf import TabularF
from .util import max_action_value
from ..policy import EGreedyPolicy, RandomPolicy
from ..utils import check_random_state


class QLearning(object):
    """
    Q-learning is a model-free reinforcement learning technique. Can be used
    to find an optimal action-selection policy for any given (finite) MDP by
    interacting with an environment.

    Parameters
    ----------
    env : Environment

    policy : the behavior policy used to generate the trajectory data

    qf : Value function (default TabularF)
        the action-value function

    alpha : float (default 0.1)
        learning rate

    gamma : float (default 0.99)
        discount factor

    n_episodes : int (default 1000)
        number of episodes

    random_state : int or RandomState
        Pseudo-random number generator state used for random sampling.
    """

    def __init__(self, env, policy=None, qf=None, alpha=0.1,
                 gamma=0.99, n_episodes=1000, random_state=None):
        self.env = env
        self.qf = qf
        self.alpha = alpha
        self.gamma = gamma
        self.n_episodes = n_episodes
        self.cur_episode = 1
        self.random_state = check_random_state(random_state)
        self.policy = policy or RandomPolicy(self.random_state)
        self.qf = qf or TabularF(self.random_state)

    def best_action_value(self, state, actions):
        return max_action_value(self.qf, state, actions)

    def learn(self):
        for _ in range(self.n_episodes):
            self.episode()

    def episode(self):
        print('Episode {self.cur_episode} / {self.n_episodes}'.format(self=self))
        self.env.reset()
        step = 1
        while not self.env.is_terminal():
            print('  Step %d' % step)
            state = self.env.cur_state()
            actions = self.env.actions(state)
            action = self.policy.action(self.qf, state, actions)
            reward, next_state = self.env.do_action(action)
            next_actions = self.env.actions(next_state)
            best_action_value = self.best_action_value(next_state, next_actions)
            td_error = reward + (self.gamma * best_action_value) - self.qf[(state, action)]
            self.qf[(state, action)] += self.alpha * td_error
            step += 1
        self.cur_episode += 1
