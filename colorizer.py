import os
from colorama import Fore, Style, init

#init for colorama to fixed windows wierdness
init()

def print_yellow(g):
    print(Fore.YELLOW, Style.BRIGHT,g,Style.RESET_ALL)

def print_red(g):
    print(Fore.RED, Style.BRIGHT,g,Style.RESET_ALL)    

def print_blue(g):
    print(Fore.BLUE, Style.BRIGHT,g,Style.RESET_ALL)

def print_green(g):
    print(Fore.GREEN, Style.BRIGHT,g,Style.RESET_ALL)
    
def input_yellow(g):
    print(Fore.YELLOW, Style.BRIGHT, end='')
    response = input(g)
    print(Style.RESET_ALL)
    return response

def input_green(g):
    print(Fore.GREEN, Style.BRIGHT, end='')
    response = input(g)
    print(Style.RESET_ALL)
    return response

def input_red(g):
    print(Fore.RED, Style.BRIGHT, end='')
    response = input(g)
    print(Style.RESET_ALL)
    return response

def input_blue(g):
    print(Fore.BLUE, Style.BRIGHT, end='')
    response = input(g)
    print(Style.RESET_ALL)
    return response

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')