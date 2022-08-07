''' Colors package'''

import colorama

colorama.init(autoreset=True)

colors = {
    'NO_COLOR': "\033[0m",
    'RED': "\033[91m",
    'GREEN': "\033[92m",
    'YELLOW': "\033[93m",
    'BLUE': '\033[94m',
    'PURPLE': "\033[95m",
    'STD_PURPLE': "\033[35m",
    'CYAN': "\033[96m",
}
