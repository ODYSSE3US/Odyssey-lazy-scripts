import colorama
import lolpython
import __init__
from colorama import Fore, Back, Style
from  lolpython import lol_py as lolpy
from __init__ import *
## FOR LINUX ONLY // Machines that support ANSI Color Coding. (Not Windows By Default)

init(autoreset=True)


Splash_ody = f"""
   {Fore.BLUE}██████{Fore.WHITE}╗ {Fore.BLUE}██████{Fore.WHITE}╗ {Fore.BLUE}██{Fore.WHITE}╗   {Fore.BLUE}██{Fore.WHITE}╗{Fore.BLUE}███████{Fore.WHITE}╗{Fore.BLUE}███████{Fore.WHITE}╗{Fore.BLUE}███████{Fore.WHITE}╗{Fore.BLUE}██{Fore.WHITE}╗   {Fore.BLUE}██{Fore.WHITE}╗{Fore.BLUE}███████{Fore.WHITE}╗{Fore.BLUE}
  ██{Fore.WHITE}╔═══{Fore.BLUE}██{Fore.WHITE}╗{Fore.BLUE}██{Fore.WHITE}╔══{Fore.BLUE}██{Fore.WHITE}╗╚{Fore.BLUE}██{Fore.WHITE}╗ {Fore.BLUE}██{Fore.WHITE}╔╝{Fore.BLUE}██{Fore.WHITE}╔════╝{Fore.BLUE}██{Fore.WHITE}╔════╝{Fore.BLUE}██{Fore.WHITE}╔════╝{Fore.BLUE}██{Fore.WHITE}║   {Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}╔════╝{Fore.BLUE}
  ██{Fore.BLUE}{Fore.WHITE}║   {Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}║  {Fore.BLUE}██{Fore.WHITE}║ ╚{Fore.BLUE}████{Fore.WHITE}╔╝ {Fore.BLUE}███████{Fore.WHITE}╗{Fore.BLUE}███████{Fore.WHITE}╗{Fore.BLUE}█████{Fore.WHITE}╗  {Fore.BLUE}██{Fore.WHITE}║   {Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}███████{Fore.WHITE}╗{Fore.BLUE}
  {Fore.BLUE}██{Fore.WHITE}║   {Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}║  {Fore.BLUE}██{Fore.WHITE}║  ╚{Fore.BLUE}██{Fore.WHITE}╔╝  ╚════{Fore.BLUE}██{Fore.WHITE}║╚════{Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}╔══╝  {Fore.BLUE}██{Fore.WHITE}║   {Fore.BLUE}██║{Fore.WHITE}╚════{Fore.BLUE}██{Fore.WHITE}║
  ╚{Fore.BLUE}██████{Fore.WHITE}╔╝{Fore.BLUE}██████{Fore.WHITE}╔╝   {Fore.BLUE}██{Fore.WHITE}║   {Fore.BLUE}███████{Fore.WHITE}║{Fore.BLUE}███████{Fore.WHITE}║{Fore.BLUE}███████{Fore.WHITE}╗╚{Fore.BLUE}██████{Fore.WHITE}╔╝{Fore.BLUE}███████{Fore.WHITE}║
   ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝
"""



def main_Menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    header = f""" {Style.BRIGHT}{Fore.RED}
♆ ODYS TOOL KIT ♆ {Fore.GREEN}
  __  __          _____ _   _ 
 |  \/  |   /\   |_   _| \ | |
 | \  / |  /  \    | | |  \| |
 | |\/| | / /\ \   | | | . ` |
 | |  | |/ ____ \ _| |_| |\  |
 |_|  |_/_/    \_|_____|_| \_|
  __  __ ______ _   _ _    _  
 |  \/  |  ____| \ | | |  | | 
 | \  / | |__  |  \| | |  | | 
 | |\/| |  __| | . ` | |  | | 
 | |  | | |____| |\  | |__| | 
 |_|  |_|______|_| \_|\____/  
_______________________________
{Fore.GREEN}Logged In As {Fore.RED} 
{Fore.GREEN}Choose An Option From The List{Fore.YELLOW}
|1|--Linux Menu
|2|--Null
|3|--Null
|4|--Null
|5|--Null
{Fore.CYAN}|02|--Dev Menu
{Fore.BLUE}|01|--Check Update
{Fore.RED}|00|--Exit {Fore.RESET}
    """
    print(header)
    choice = input(Fore.WHITE + Style.BRIGHT + "|MAIN MENU:> ")
    os.system('cls' if os.name == 'nt' else 'clear')
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "01":
        check_updates()
    elif choice =="02":
        dev_Menu()
    elif choice == "00":
        clearScr(), os._exit(n)
    elif choice == "":
        print(Fore.RED + Style.BRIGHT +"Invalid Command...")
        sleep(1)
        main_Menu()
    else:
        print(Fore.RED + Style.BRIGHT +"Command Not Reccognised...")
        sleep(1)
        main_Menu()



def dev_Menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    header_dev = f""" {Style.BRIGHT}{Fore.RED}
♆ ODYS TOOL KIT ♆ {Fore.GREEN}
     _____  ________      __ 
    |  __ \|  ____\ \    / / 
    | |  | | |__   \ \  / /  
    | |  | |  __|   \ \/ /   
    | |__| | |____   \  /    
    |_____/|______|   \/     
  __  __ ______ _   _ _    _ 
 |  \/  |  ____| \ | | |  | |
 | \  / | |__  |  \| | |  | |
 | |\/| |  __| | . ` | |  | |
 | |  | | |____| |\  | |__| |
 |_|  |_|______|_| \_|\____/ 
_______________________________
{Fore.GREEN}Developer Menu For Custom Scripts{Fore.YELLOW}
|1|--Get Object Id's
|2|--List Communites
|3|--Generate Transaction ID
|4|--System Infomation
|5|--Send Active Object
{Fore.CYAN}|01|--MAIN MENU
{Fore.RED}|00|--Exit {Fore.RESET}
    """
    print(header_dev)
    choice = input(Fore.WHITE + Style.BRIGHT + "/DEVELOPER MENU:> ")
    os.system('cls' if os.name == 'nt' else 'clear')
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "01":
        main_Menu()
    elif choice == "00":
        clearScr(), sys.exit()
    elif choice == "":
        print(Fore.RED + Style.BRIGHT +"Invalid Command...")
        sleep(1)
        dev_Menu()
    else:
        print(Fore.RED + Style.BRIGHT +"Command Not Reccognised...")
        sleep(1)
        dev_Menu()



def dev_Menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    if os.name == 'nt':
        print("This Menu Is Incompatible With {os.name}, To Continue Please Use A Linux Distribution.")
        input("Press Any Key To Return Home:> ")
        main_Menu()
    else:
        pass
    header_dev = f""" {Style.BRIGHT}{Fore.RED}
♆ ODYS TOOL KIT ♆ {Fore.GREEN}
  _      _____ _   _ _    ___   __
 | |    |_   _| \ | | |  | \ \ / /
 | |      | | |  \| | |  | |\ V / 
 | |      | | | . ` | |  | | > <  
 | |____ _| |_| |\  | |__| |/ . \ 
 |______|_____|_| \_|\____//_/ \_\
   |  \/  |  ____| \ | | |  | |   
   | \  / | |__  |  \| | |  | |   
   | |\/| |  __| | . ` | |  | |   
   | |  | | |____| |\  | |__| |   
   |_|  |_|______|_| \_|\____/    
_____________________________________
{Fore.GREEN}Linux Only Scripts; Select a Base Distro{Fore.YELLOW}
|1|--Arch
|2|--Debian
|3|--Ubuntu
|4|--Fedora
|5|--GNU/UNIX (Other)
{Fore.CYAN}|01|--MAIN MENU
{Fore.RED}|00|--Exit {Fore.RESET}
    """
    print(header_dev)
    choice = input(Fore.WHITE + Style.BRIGHT + "/DEVELOPER MENU:> ")
    os.system('cls' if os.name == 'nt' else 'clear')
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "01":
        main_Menu()
    elif choice == "00":
        clearScr(), sys.exit()
    elif choice == "":
        print(Fore.RED + Style.BRIGHT +"Invalid Command...")
        sleep(1)
        dev_Menu()
    else:
        print(Fore.RED + Style.BRIGHT +"Command Not Reccognised...")
        sleep(1)
        dev_Menu()
