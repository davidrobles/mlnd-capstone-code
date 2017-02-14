from __future__ import print_function


def print_header(text):
    l = len(text) + 2
    print('-' * l)
    print(' {} '.format(text))
    print('-' * l, end='\n\n')
