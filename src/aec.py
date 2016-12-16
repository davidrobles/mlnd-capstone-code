from __future__ import print_function

def str_aec(text, color):
    """Returns text wrapped by the given ansi color code"""
    AEC_COLORS = {
        'black': (0, 30),
        'red': (0, 31),
        'green': (0, 32),
        'yellow': (0, 33),
        'blue': (0, 34),
        'purple': (0, 35),
        'cyan': (0, 36),
        'light_gray': (0, 37),
        'dark_gray': (0, 30),
        'bold_red': (1, 31),
        'bold_green': (1, 32),
        'bold_yellow': (1, 33),
        'bold_blue': (1, 34),
        'bold_purple': (1, 35),
        'bold_cyan': (1, 36),
        'white': (1, 37)
    }
    color = color.lower()
    if color not in AEC_COLORS:
        raise Exception(u"AEC color '{0}' does not exist".format(color))
    a, b = AEC_COLORS[color]
    return u'\033[{0};{1}m{2}\033[0m'.format(a, b, text)

def print_aec(text, color, end='\n'):
    """Prints text wrapped by the given ansi color code"""
    print(str_aec(text, color), end=end)
