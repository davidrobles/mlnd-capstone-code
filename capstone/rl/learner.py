import abc
import six
from .utils import CallbackList


@six.add_metaclass(abc.ABCMeta)
class Learner(object):

    def __init__(self, env, n_episodes=1000, callbacks=None, verbose=True):
        self.env = env
        self.n_episodes = n_episodes
        self.callbacks = CallbackList(callbacks)
        self.verbose = verbose

    def learn(self):
        '''Trains the model for a fixed number of episodes.'''
        self.callbacks.on_train_begin()
        for episode in range(self.n_episodes):
            self.callbacks.on_episode_begin(episode)
            self.env.reset()
            self.episode()
            self.callbacks.on_episode_end(episode, self.qf)
        self.callbacks.on_train_end(self.qf)

    @abc.abstractmethod
    def episode(self):
        pass
