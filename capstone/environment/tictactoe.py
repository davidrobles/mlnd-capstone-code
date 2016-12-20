from . import Environment


class TicTacToeEnv(Environment):

    def __init__(self, game_mdp):
        self.game_mdp = game_mdp
        self.reset()

    def cur_state(self):
        return self.game.copy()

    def actions(self):
        return self.game_mdp.actions(self.game)

    def do_action(self, action):
        prev = self.game.copy()
        self.game.make_move(action)
        return self.game_mdp.reward(prev, action, self.game)

    def reset(self):
        self.game = self.game_mdp.start_state()
