from ...utils import check_random_state

_MEAN = 0.0
_STD = 0.3


class TabularQ(dict):

    def __init__(self, random_state=None):
        self.random_state = check_random_state(random_state)

    def __getitem__(self, key):
        if key not in self:
            state, action = key
            if action is None:
                self[key] = 0
            else:
                self[key] = self.random_state.normal(_MEAN, _STD)
        return super(TabularQ, self).__getitem__(key)
