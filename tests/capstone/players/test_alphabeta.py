import unittest
from capstone.players import AlphaBeta


class TestAlphaBeta(unittest.TestCase):

    def setUp(self):
        self.ab = AlphaBeta()

    def test_has_name(self):
        self.assertEqual(AlphaBeta.name, "Alpha-Beta Pruning")

    def test_can_instantiate(self):
        pass
