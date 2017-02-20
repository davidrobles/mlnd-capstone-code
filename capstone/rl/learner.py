import abc
import six


@six.add_metaclass(abc.ABCMeta)
class Learner(object):

    def __init__(self, env, n_episodes=1000, verbose=True):
        self.env = env
        self.n_episodes = n_episodes
        self.verbose = verbose
        self.cur_episode = 1

    def learn(self):
        for _ in range(self.n_episodes):
            self.episode()

    def episode(self):
        if self.verbose:
            print('Episode {self.cur_episode} / {self.n_episodes}'.format(self=self))
        self.env.reset()
        while not self.env.is_terminal():
            self.step()
        self.cur_episode += 1

    @abc.abstractmethod
    def step(self):
        pass
