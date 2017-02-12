import random


class TabularQF(dict):

    def __getitem__(self, key):
        if key not in self:
            self[key] = random.random() - 0.5
        return super(TabularQF, self).__getitem__(key)
