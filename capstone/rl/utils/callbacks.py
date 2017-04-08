class CallbackList(object):
    '''Container abstracting a list of callbacks (inspired by Keras).'''

    def __init__(self, callbacks=None):
        self.callbacks = callbacks or []

    def on_episode_begin(self, episode, qf):
        '''Called at the beginning of every episode.'''
        for callback in self.callbacks:
            callback.on_episode_begin(episode, qf)

    def on_episode_end(self, episode, qf):
        '''Called at the end of every episode.'''
        for callback in self.callbacks:
            callback.on_episode_end(episode, qf)

    def on_train_begin(self):
        '''Called at the beginning of model training.'''
        for callback in self.callbacks:
            callback.on_train_begin()

    def on_train_end(self, qf):
        '''Called at the end of model training.'''
        for callback in self.callbacks:
            callback.on_train_end(qf)


class Callback(object):
    '''Abstract base class used to build new callbacks (inspired by Keras).'''

    def on_episode_begin(self, episode, qf):
        '''Called at the beginning of every episode.'''
        pass

    def on_episode_end(self, episode, qf):
        '''Called at the end of every episode.'''
        pass

    def on_train_begin(self):
        '''Called at the beginning of model training.'''
        pass

    def on_train_end(self, qf):
        '''Called at the end of model training.'''
        pass
