import unittest
from capstone.player import AlphaBeta


class TestAlphaBeta(unittest.TestCase):

    def setUp(self):
        self.ab = AlphaBeta()

    def test_name(self):
        self.assertEqual(AlphaBeta.name, 'Alpha-Beta')
        self.assertEqual(self.ab.name, 'Alpha-Beta')
