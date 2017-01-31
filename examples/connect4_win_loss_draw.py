from capstone.util import c42pdf

win = [[' ', ' ', ' ', 'O', 'X', ' ', ' '],
       [' ', ' ', 'O', 'X', 'X', ' ', ' '],
       [' ', ' ', 'X', 'O', 'O', ' ', ' '],
       [' ', 'X', 'O', 'O', 'X', ' ', ' '],
       ['O', 'X', 'X', 'X', 'O', ' ', ' '],
       ['O', 'X', 'X', 'O', 'O', ' ', ' ']]
c42pdf(win, 'figures/c4_env_win.pdf')

loss = [[' ', ' ', 'X', ' ', ' ', ' ', ' '],
        [' ', ' ', 'O', ' ', 'X', ' ', ' '],
        [' ', ' ', 'O', 'O', 'X', 'X', 'X'],
        [' ', ' ', 'X', 'X', 'O', 'O', 'O'],
        [' ', 'X', 'O', 'O', 'X', 'O', 'O'],
        [' ', 'O', 'X', 'O', 'X', 'O', 'X']]
c42pdf(loss, 'figures/c4_env_loss.pdf')

draw = [['X', 'X', 'O', 'X', 'X', 'O', 'O'],
        ['O', 'X', 'X', 'O', 'O', 'X', 'X'],
        ['X', 'O', 'X', 'X', 'X', 'O', 'O'],
        ['O', 'X', 'O', 'O', 'O', 'X', 'X'],
        ['X', 'O', 'O', 'X', 'X', 'O', 'O'],
        ['O', 'X', 'O', 'O', 'X', 'X', 'O']]
c42pdf(draw, 'figures/c4_env_draw.pdf')
