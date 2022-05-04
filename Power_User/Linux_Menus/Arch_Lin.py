import colorama
import os
import sys
import time

from time import sleep
from colorama import Fore, Back, Style, init
colorama.init(autoreset=True)

FB = Fore.BLUE + Style.NORMAL # {FB}
FR = Style.RESET_ALL + Fore.RESET + Back.RESET #{FR}
FW = Fore.WHITE + Style.BRIGHT # {FW}
BB = Back.BLUE + Fore.BLACK # {BB}
FG = Fore.GREEN
BG = Back.GREEN + Fore.BLACK
FY = Fore.YELLOW
FC = Fore.CYAN
FR = Fore.RED
BRR = Back.RED + Fore.BLACK
BKRE = Back.RESET
Full_Blue = Back.BLUE + Fore.BLUE

def ArchLogo():
    ArchLogo = f"""

                  {FB}▄     {FW}                                          _____   _____ _    _   _      _____ _   _ _    ___   __
                 {FB}▄█▄        {FW}                                /\   |  __ \ / ____| |  | | | |    |_   _| \ | | |  | \ \ / /
               {FB}▄█████▄          {FW}                           /  \  | |__) | |    | |__| | | |      | | |  \| | |  | |\ V / 
              {FB}▄███████▄             {FW}                      / /\ \ |  _  /| |    |  __  | | |      | | | . ` | |  | | > <  
             {FB}▄ ▀▀██████▄                {FW}                 / ____ \| | \ \| |____| |  | | | |____ _| |_| |\  | |__| |/ . \       
            {FB}▄██▄▄ ▀█████▄                   {FW}        ____/_/____\_\_|__\_\______|_|_ |_|_|______|_____|_|_\_|\____//_/ \_\ _____ 
           {FB}▄█████████████▄                      {FW}   / ____|  ____|__   __|   | |  | |  __ \  |__   __/ __ \ / __ \| |     / ____|
          {FB}▄███████████████▄                       {FW}| (___ | |__     | |______| |  | | |__) |    | | | |  | | |  | | |    | (___  
         {FB}▄█████████████████▄                       {FW}\___ \|  __|    | |______| |  | |  ___/     | | | |  | | |  | | |     \___ \ 
        {FB}▄███████████████████▄                      {FW}____) | |____   | |      | |__| | |         | | | |__| | |__| | |____ ____) |
       {FB}▄█████████▀▀▀▀████████▄                    {FW}|_____/|______|  |_|       \____/|_|         |_|  \____/ \____/|______|_____/ {FR}
      {FB}▄████████▀      ▀███████▄                             
     {FB}▄█████████        ████▀▀██▄                            
    {FB}▄██████████        █████▄▄▄                             
   {FB}▄██████████▀        ▀█████████▄                          
  {FB}▄██████▀▀▀              ▀▀██████▄                         
 {FB}▄███▀▀                       ▀▀███▄                        
{FB}▄▀▀                               ▀▀▄{FR}

{Full_Blue}___________________________________________________________________________________________________________________________________________
    """
    os.system("clear")
    print(ArchLogo)


ArchInstruct = f"""
  {FG}The {FB}Black Arch {FG}Linux Repository Has Been {BG}Successfully{BKRE}{FG} Installed
  _______________________________________________________________
  {FY}# To list all of the available tools, run
  {FC}$ sudo pacman -Sgg | grep blackarch | cut -d' ' -f2 | sort -u
  
  {FY}# To install all of the tools, run
  {FC}$ sudo pacman -S blackarch
  
  {FY}# To install a category of tools, run
  {FC}$ sudo pacman -S blackarch-<category>
  
  {FY}# To see the blackarch categories, run
  {FC}$ sudo pacman -Sg | grep blackarch
  
  {FY}# Note - it maybe be necessary to overwrite certain packages when installing blackarch tools. If
  you experience {FRR}'failed to commit transaction'{FY} errors, use the {BR}--needed{BKRE} {FY}and {BR}--overwrite{BKRE} {FY}switches
  {FY}# For example:
  {FC}$ sudo pacman -Syyu --needed blackarch --overwrite='*'


"""


ArchLogo()
DefaultInst = input("Would You Like To Install The Reccomended Packages? |Y/N| ")
if DefaultInst == "Y" or "y":
    os.system("sudo pacman -Syu") # Updates The System
    os.system("sudo pacman -Syy") # Updates The Database
    os.system("pacman -S wine") # Windows Compatibility Layer
    os.system("pacman -S git") # Github
    os.system("pacman -S wget") # Download Things From The Terminal
    os.system("pacman -S curl") # A URL Retrieval Utility & Library
    os.system("pacman -S vscode") # All In One IDE, To Simplify Workflow. 
    os.system("pacman -S cmatrix") # Hacker Mode lol
    os.system("pacman -S figlet") # Powerful ASCII Art Text Generator
    os.system("pacman -S toilet") # ASCII Text Generator
    os.system("pacman -S lolcat") # Feel The Rainbow, Taste The Rainbow... 
    os.system("pacman -S nemo") # File explorer thats compatible with black arch
    os.system("pacman -S nano") # A simple yet powerful text editor
    os.system("pacman -S vim") # An Overcomplicated Text Editor
    os.system("pacman -S Discord") # Its Discord, Duh.
    os.system("pacman -S signal-desktop") # Open-Source Privacy Orientated Instant-Messenger
    os.system("pacman -S flameshot") # Screenshot Tool With Direct Upload
    os.system("pacman -S audacious") # Low resource music player
    os.system("pacman -S thunderbird") # Email Client
    os.system("pacman -S snapd") # Snap Package Manager - Also installs go & go-tools.
    #os.system("pacman -S ") 
    

else:
    pass #return to menu

finally:
    ArchLogo()
    RepoInst = input("Would You Like To Install The Black Arch Repo? |Y/N|")
    if RepoInst == "Y" or "y":
        #os.sys("sudo su") #Requires Superuser
        os.sys("curl -O https://blackarch.org/strap.sh")
        os.sys("sudo chmod +x strap.sh && ./strap.sh")
        os.sys("sudo pacman -Syu")
        #os.sys("")
        ArchLogo()
        print(ArchInstruct)
        input("Press Any Key To Return To The Menu|> ")
        #Menu Funct Here


    else:
        pass #return to menu