import abc
import six


@six.add_metaclass(abc.ABCMeta)
class ValueFunction(object):

    @abc.abstractmethod
    def __getitem__(self, s_or_sa):
        '''Takes a state or a stat-action tuple'''
        pass
