import lexer
import parser
import shutil
import platform
import os
from datetime import datetime
from colorama import *
init()

parser.env = "ide"
print(Fore.YELLOW)
print(" Kestrel ".center(shutil.get_terminal_size().columns, "="))
print(f"Kestrel 1.0.1 on {os.name.lower()} {platform.system().lower()} ({platform.release().lower()})".center(shutil.get_terminal_size().columns))
print(Style.RESET_ALL)

while True:
    try:
        now = datetime.now()
        s = input(f'{Fore.LIGHTYELLOW_EX}[{now.strftime("%H:%M:%S")}]{Fore.YELLOW}{Style.BRIGHT} -> {Style.RESET_ALL}')
    except EOFError:
        break
    result = parser.parser.parse(s)
    print(result)
