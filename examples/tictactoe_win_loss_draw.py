from capstone.util import tic2pdf

tic2pdf('figures/tic_env_win.pdf', [['X', 'O', 'X'],
                                    ['O', 'X', ' '],
                                    ['X', ' ', 'O']])

tic2pdf('figures/tic_env_loss.pdf', [['X', 'X', 'O'],
                                     [' ', 'O', ' '],
                                     ['O', ' ', 'X']])

tic2pdf('figures/tic_env_draw.pdf', [['X', 'X', 'O'],
                                     ['O', 'O', 'X'],
                                     ['X', 'O', 'X']])
