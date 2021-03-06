import unittest
from capstone.rl.policies import EGreedy


class FakeEnv(object):

    def __init__(self):
        self._actions = []

    def cur_state(self):
        return 'FakeState'

    def actions(self, state):
        return self._actions


class TestEGreedy(unittest.TestCase):

    def setUp(self):
        self.policy = EGreedy(0.1)
        self.env = FakeEnv()

    # def test_max_action(self):
    #     cur_state = self.env.cur_state()
    #     self.env._actions = [1, 5, 8]
    #     fake_qf = {
    #         (cur_state, 1): 5,
    #         (cur_state, 5): 33,
    #         (cur_state, 8): 23,
    #     }
    #     action = self.policy.action(self.env, qf=fake_qf)
    #     self.assertEqual(action, 5)

    # def test_raises_value_error_if_no_actions_available(self):
    #     self.env._actions = []
    #     with self.assertRaises(ValueError):
    #         self.policy.action(self.env)
