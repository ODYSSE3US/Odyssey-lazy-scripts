import colorama
import lolpython
import time
import os
import pathlib
#import blessings
from colorama import Fore, Back, Style, init
from  lolpython import lol_py as lolpy
from time import sleep
#from blessings import Terminal

#t = Terminal()

init(autoreset=True)


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







Splash_ody = f"""
   ██████╗ ██████╗ ██╗   ██╗███████╗███████╗███████╗██╗   ██╗███████╗
  ██╔═══██╗██╔══██╗╚██╗ ██╔╝██╔════╝██╔════╝██╔════╝██║   ██║██╔════╝
  ██║   ██║██║  ██║ ╚████╔╝ ███████╗███████╗█████╗  ██║   ██║███████╗
  ██║   ██║██║  ██║  ╚██╔╝  ╚════██║╚════██║██╔══╝  ██║   ██║╚════██║
  ╚██████╔╝██████╔╝   ██║   ███████║███████║███████╗╚██████╔╝███████║
   ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝
"""


example=f"{Fore.RED}SOMETHING COOL"


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


lolpy(Splash_ody) ## FOR LINUX ONLY // Machines that support ANSI Color Coding. (Not Windows By Default)


#print("=" * 10)
#print(ArchLogo)

print(pathlib.Path().resolve())