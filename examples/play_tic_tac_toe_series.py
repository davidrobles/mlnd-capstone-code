import sys
sys.path.insert(0, '/home/drobles/projects/mlnd-capstone-code/src/')
from games import TicTacToe
from players import RandPlayer
from utils import play_series

game = TicTacToe()
players = [RandPlayer(), RandPlayer()]
play_series(game, players)
