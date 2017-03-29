from .callbacks import Callback


class LinearAnnealing(Callback):

    def __init__(self, obj, param, init, final, n_episodes):
        self.doing = 'inc' if init < final else 'dec'
        self.obj = obj
        self.param = param
        self.init = init
        self.final = final
        self.n_episodes = n_episodes
        self.change_rate = (final - init) / n_episodes
        print('change rate: %f' % self.change_rate)

    def on_episode_end(self, episode, qf):
        if ((self.doing == 'inc' and getattr(self.obj, self.param) < self.final) or
            (self.doing == 'dec' and getattr(self.obj, self.param) > self.final)):
                prev = getattr(self.obj, self.param)
                setattr(self.obj, self.param, prev + self.change_rate)
                print('New epsilon: {}'.format(getattr(self.obj, self.param)))
