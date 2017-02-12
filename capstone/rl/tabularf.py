import random


class TabularF(dict):
    '''
    Tabular representation for any of the two types of value functions:

    1. state value function (V-Functions).
       e.g.
       vf = TabularF()
       vf[state] = 1

    2. state-action value functions (Q-functions)
       e.g.
       qf = TabularF()
       qf[(state, action)] = 1

    '''

    def __getitem__(self, key):
        if key not in self:
            self[key] = random.random() - 0.5
        return super(TabularF, self).__getitem__(key)
