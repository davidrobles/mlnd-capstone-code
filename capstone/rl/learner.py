import abc
import six
from .utils import CallbackList


@six.add_metaclass(abc.ABCMeta)
class Learner(object):

    def __init__(self, env):
        self.env = env

    def train(self, n_episodes, callbacks=None):
        '''Trains the model for a fixed number of episodes.'''
        callbacks = CallbackList(callbacks)
        callbacks.on_train_begin()
        for episode in range(n_episodes):
            callbacks.on_episode_begin(episode, self.qfunction)
            self.env.reset()
            self.episode()
            callbacks.on_episode_end(episode, self.qfunction)
        callbacks.on_train_end(self.qfunction)

    @abc.abstractmethod
    def episode(self):
        pass
