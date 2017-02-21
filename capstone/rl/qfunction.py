import abc
import six


@six.add_metaclass(abc.ABCMeta)
class QFunction(object):

    @abc.abstractmethod
    def __getitem__(self, state_action):
        pass
