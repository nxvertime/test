from colorama import Fore, init

init()


## make colors usage more simple :)
red = Fore.RED
lightRed = Fore.LIGHTRED_EX

blue = Fore.BLUE
lightBlue = Fore.LIGHTBLUE_EX

green = Fore.GREEN
lightGreen = Fore.LIGHTGREEN_EX

yellow = Fore.YELLOW
lightYellow = Fore.LIGHTYELLOW_EX

magenta = Fore.MAGENTA
lightMagenta = Fore.LIGHTMAGENTA_EX

cyan = Fore.CYAN
lightCyan = Fore.LIGHTCYAN_EX

white = Fore.RESET

black = Fore.BLACK

reset = Fore.RESET


attention = f'{reset}[{yellow}!{reset}] '
info = f'{reset}[{cyan}*{reset}] '
ok = f'{reset}[{lightGreen}ok{reset}] '
success = f'{reset}[{green}v{reset}] '
error = f'{reset}[{yellow}!{reset}] '
question = f'{reset}[{lightGreen}?{reset}] '
sub = f'{reset}[{lightGreen}+{reset}] '

#by nxvertime, no writes reserved lol :)
