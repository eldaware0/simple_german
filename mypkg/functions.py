
from colorama import Fore


def print_wcolor(color, text):
    """Prints text in a color. Next call prints text in red:
    print_wcolor("red", some_text). For more details read in colorama lib
    """
    assert type(color) == str
    assert type(text)  == str

    if color.upper() == 'RED':
        print(Fore.RED + text + Fore.RESET)
    elif color.upper() == 'BLUE':
        print(Fore.BLUE + text + Fore.RESET)
    elif color.upper() == 'GREEN':
        print(Fore.GREEN + text + Fore.RESET)
    else:
        raise NotImplementedError()