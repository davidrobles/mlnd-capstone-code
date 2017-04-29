from ..value_function import ValueFunction
from ...utils import check_random_state

_MEAN = 0.0
_STD = 0.3


class TabularVF(ValueFunction):
    '''
    Tabular Value Function.

    Can be used for both state V(s) and state-action Q(s, a) values.

    # Arguments
        init: boolean. Wheter to return a randomly initialized value
            when accessed and does not exist in the table.

    # Example
        ```python
        >>> v = TabularVF()
        >>> v[state] = 3.2
        >>> print(q[state])
        3.2

        >>> q = TabularVF()
        >>> q[state, action] = 1.8
        >>> print(q[state, action])
        1.8
        ```
    '''

    def __init__(self, init=True, random_state=None):
        self.init = init
        self.random_state = check_random_state(random_state)
        self._table = {}

    def __setitem__(self, key, value):
        '''
        Sets the state or state-action value.

        # Arguments
            key: `state` or `(state, action)`
            value: a scalar
        '''
        self._table[key] = value

    #################
    # ValueFunction #
    #################

    def __getitem__(self, key):
        '''
        Returns the state or state-action value.

        # Arguments
            key: `state` or `(state, action)`
        # Returns
            a scalar value.
        '''
        if key not in self._table:
            if self.init:
                self._table[key] = self.random_state.normal(_MEAN, _STD)
            else:
                self._table[key] = 0
        return self._table[key]
