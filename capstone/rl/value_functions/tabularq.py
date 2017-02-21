from ..qfunction import QFunction
from ...utils import check_random_state

_MEAN = 0.0
_STD = 0.3


class TabularQ(QFunction):

    def __init__(self, init=True, random_state=None):
        self.init = init
        self.random_state = check_random_state(random_state)
        self._d = {}

    def __setitem__(self, key, value):
        self._d[key] = value

    #############
    # QFunction #
    #############

    def __getitem__(self, key):
        if key not in self._d:
            state, action = key
            if action is None or not self.init:
                self._d[key] = 0
            else:
                self._d[key] = self.random_state.normal(_MEAN, _STD)
        return self._d[key]
