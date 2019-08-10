MAGENTA = '\033[95m',
DARKMAGENTA = '\033[35m',
CYAN = '\033[96m',
DARKCYAN = '\033[36m',
BLUE = '\033[94m',
DARKBLUE = '\033[34m',
GREEN = '\033[92m',
DARKGREEN = '\033[32m',
YELLOW = '\033[93m',
DARKYELLOW = '\033[33m',
RED = '\033[91m',
DARKRED = '\033[31m',
BOLD = '\033[1m',
UNDERLINE = '\033[4m',
END = '\033[0m'

COLORS = [MAGENTA, CYAN, BLUE, GREEN, YELLOW, RED]


def style(text, *color):
    prefix = ''.join(color)
    ends = END*len(color)
    return f'{prefix}{text}{ends}'


def style_unique(*text):
    return [style(x, col) for x, col in zip(text, COLORS)]
