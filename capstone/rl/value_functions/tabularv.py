from ..value_function import ValueFunction
from ...utils import check_random_state

_MEAN = 0.0
_STD = 0.3


class TabularV(ValueFunction):
    ''' Tabular V-Function'''

    def __init__(self, init=True, random_state=None):
        self.init = init
        self.rs = check_random_state(random_state)
        self._d = {}

    def __setitem__(self, state, value):
        self._d[state] = value

    ##################
    # Value Function #
    ##################

    def __getitem__(self, state):
        ''' V(s) '''
        assert state is not None
        assert state is not tuple
        if state not in self._d:
            if self.init:
                print('init')
                self._d[state] = self.rs.normal(_MEAN, _STD)
            else:
                print('set to 0')
                self._d[state] = 0
        return self._d[state]
