import sys
sys.path.insert(0, '/home/drobles/projects/mlnd-capstone-code/src/')
from players import RandPlayer
from tictactoe import TicTacToe
from utils import play_series

game = TicTacToe()
players = [RandPlayer(), RandPlayer()]
play_series(game, players)
