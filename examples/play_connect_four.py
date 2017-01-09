from capstone.game import Connect4
from capstone.player import RandPlayer
from capstone.util import play_match

game = Connect4()
# game.set_board(
# 	[['-', '-', '-', '-', '-', '-', '-'],
# 	 ['-', '-', '-', '-', '-', '-', '-'],
# 	 ['-', '-', '-', '-', '-', '-', '-'],
# 	 ['-', '-', '-', '-', '-', '-', '-'],
# 	 ['-', 'X', '-', '-', '-', '-', '-'],
# 	 ['X', 'O', 'O', '-', '-', '-', '-']]
# )

# game.set_board(
# 	[['-', 'O', 'X', '-', 'O', '-', '-'],
# 	 ['-', 'X', 'O', '-', 'X', '-', 'X'],
# 	 ['X', 'O', 'X', '-', 'X', '-', 'O'],
# 	 ['O', '-', 'O', 'O', 'O', 'X', 'X'],
# 	 ['O', 'O', 'X', 'X', 'O', 'X', 'O'],
# 	 ['O', 'X', 'O', 'X', 'X', 'X', 'O']]
# )

# print('game')
# print(game._check_win(game._boards[0]))

# print("{0:b}".format(game._boards[0]))
# print(bool(game._boards[0] & (1 << 20)))

# print('H1: {}'.format(Connect4.H1))
# print('H2: {}'.format(Connect4.H2))
# print('SIZE: {}'.format(Connect4.SIZE))
# print('SIZE1: {}'.format(Connect4.SIZE1))
# print('ALL1')
# game.print_bitboard(Connect4.ALL1)
# print('COL1')
# game.print_bitboard(Connect4.COL1)
# print('BOTTOM')
# game.print_bitboard(Connect4.BOTTOM)
# print('TOP')
# game.print_bitboard(Connect4.TOP)
# print('BUENO')
# print(game)

# print(game.ALL1)

players = [RandPlayer(), RandPlayer()]
play_match(game, players)



# print(game)
# game.make_move(0)
# print(game)
# game.make_move(0)
# print(game)
