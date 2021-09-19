import sys
import time
from colorama import init, Fore
import subprocess, platform
init(strip=not sys.stdout.isatty()) 
init(autoreset=True)
init(convert=True)
from termcolor import colored, cprint 
from pyfiglet import figlet_format

vapeConfig = "81ef04ad-bf68-419e-953b-7ef862a800fd"

while True:
    cprint(figlet_format('  Conrad Configs', font='big'), 'cyan', attrs=['bold'])
    print(f'{Fore.LIGHTCYAN_EX}--------------------------------')
    print(f'        {Fore.CYAN}[{Fore.RED}1{Fore.CYAN}]{Fore.GREEN} Novoline@Intent')
    print(f'        {Fore.CYAN}[{Fore.RED}2{Fore.CYAN}]{Fore.MAGENTA} Novline.wtf')
    print(f'        {Fore.CYAN}[{Fore.RED}3{Fore.CYAN}]{Fore.CYAN} Rise')
    print(f'        {Fore.CYAN}[{Fore.RED}4{Fore.CYAN}]{Fore.GREEN} VapeV4')
    print(f'        {Fore.CYAN}[{Fore.RED}5{Fore.CYAN}]{Fore.RED} Azura')
    print(f'        {Fore.CYAN}[{Fore.RED}6{Fore.CYAN}]{Fore.MAGENTA} Moon')
    print(f'{Fore.LIGHTCYAN_EX}--------------------------------')
    print(' ')
    print(f'{Fore.CYAN}What client would you like a config for?')
    x = input()
    if x == "1":
        print(f'{Fore.GREEN}Fetching download link. Please wait...')
    elif x == "2":
        print(f'{Fore.GREEN}Fetching download link. Please wait...')
    elif x == "3":
        print(f'{Fore.GREEN}Fetching download link. Please wait...')
    elif x == "4":
        print(f'{Fore.GREEN}Fetching config code. Please wait...')
        time.sleep(0.700)
        print(' ')
        print(f'{Fore.GREEN}Cofing code found! {vapeConfig}')
    elif x == "5":
        print(f'{Fore.GREEN}Fetching download link. Please wait...')
    elif x == "6":
        print(f'{Fore.GREEN}Fetching download link. Please wait...')
    elif x == "":
        exit()
    if x.isalpha():
        print(f'{Fore.RED}Did you fr just type a letter?')
        time.sleep(3)
        if platform.system()=="Windows":
            subprocess.Popen("cls", shell=True).communicate() #I like to use this instead of subprocess.call since for multi-word commands you can just type it out, granted this is just cls and subprocess.call should work fine 
        else: #Linux and Mac
            print("\033c", end="")
    else:
        print(' ')
        print(f'{Fore.CYAN}Press ENTER to download another config or type "x" to close the application')
        z = input()
        if z.lower() == "x":
            break
        if platform.system()=="Windows":
            subprocess.Popen("cls", shell=True).communicate() #I like to use this instead of subprocess.call since for multi-word commands you can just type it out, granted this is just cls and subprocess.call should work fine 
        else: #Linux and Mac
            print("\033c", end="")

