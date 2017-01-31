from capstone.util import tic2pdf

win = [['X', 'O', 'X'],
       ['O', 'X', ' '],
       ['X', ' ', 'O']]
tic2pdf(win, 'figures/tic_env_win.pdf')

loss = [['X', 'X', 'O'],
        [' ', 'O', ' '],
        ['O', ' ', 'X']]
tic2pdf(loss, 'figures/tic_env_loss.pdf')

draw = [['X', 'X', 'O'],
        ['O', 'O', 'X'],
        ['X', 'O', 'X']]
tic2pdf(draw, 'figures/tic_env_draw.pdf')
