#!/bin/bash


RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
ORANGE='\033[0;33m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color





echo ARCH Installer Script
echo "Would You Like To Install The Reccomended Packages?"
read -p "Continue (y/n)?" CONT
if [ "$CONT" = "y" ]; then
  mkdir Github
  mkdir Hacking_Tools
  mkdir VS_Code_Projects
  sudo pacman -Syu # Updates The System
  sudo pacman -Syy # Updates The Database
  pacman -S wine # Windows Compatibility Layer
  pacman -S git # Github
  pacman -S python # Python 2 (Depricated)
  pacman -S python3 # Python 3 Latest Scripting Language
  pacman -S wget # Download Things From The Terminal
  pacman -S curl # A URL Retrieval Utility & Library
  pacman -S vscode # All In One IDE, To Simplify Workflow. 
  pacman -S cmatrix # Hacker Mode lol
  pacman -S figlet # Powerful ASCII Art Text Generator
  pacman -S lolcat # Feel The Rainbow, Taste The Rainbow...
  pacman -S toilet # ASCII Text Generator
  pacman -S nemo # File explorer thats compatible with black arch
  pacman -S nano # A simple yet powerful text editor
  pacman -S vim # An Overcomplicated Text Editor
  pacman -S Discord # Its Discord, Duh.
  pacman -S signal-desktop # Open-Source Privacy Orientated Instant-Messenger
  pacman -S flameshot # Screenshot Tool With Direct Upload
  pacman -S audacious # Low resource music player
  pacman -S thunderbird # Email Client
  pacman -S snapd # Snap Package Manager - Also installs go & go-tools.
  #pacman -S Package_Name
  exit;

elif [ "$CONT" = "n" ]; then
  printf "Would You Like To Install The ${BLUE}BlackArch${NC} Repository?"
  printf "${RED}WARNING: This Requires Root Privleges.${NC}"
  read -p "Continue (y/n)?" CONFI
  if [ "$CONFI" = "y" ]; then
  sudo su
  curl -O https://blackarch.org/strap.sh
  chmod +x strap.sh
  sudo ./strap.sh
  sudo pacman -Syu

  Instructions="${YELLOW}# To list all of the available tools, run\n${CYAN}$ sudo pacman -Sgg | grep blackarch | cut -d' ' -f2 | sort -u\n\n${YELLOW}# To install all of the tools, run\n${CYAN}$ sudo pacman -S blackarch\n\n${YELLOW}# To install a category of tools, run\n${CYAN}$ sudo pacman -S blackarch-<category>\n\n${YELLOW}# To see the blackarch categories, run\n${CYAN}$ sudo pacman -Sg | grep blackarch\n\n${YELLOW}# Note - it maybe be necessary to overwrite certain packages when installing blackarch tools. If\n# you experience ${RED}'failed to commit transaction'${YELLOW} errors, use the --needed and --overwrite switches\n${YELLOW}# For example:${NC}\n${CYAN}$ sudo pacman -Syyu --needed blackarch --overwrite='*'\n"

  printf "${YELLOW}# To list all of the available tools, run\n${CYAN}$ sudo pacman -Sgg | grep blackarch | cut -d' ' -f2 | sort -u\n\n${YELLOW}# To install all of the tools, run\n${CYAN}$ sudo pacman -S blackarch\n\n${YELLOW}# To install a category of tools, run\n${CYAN}$ sudo pacman -S blackarch-<category>\n\n${YELLOW}# To see the blackarch categories, run\n${CYAN}$ sudo pacman -Sg | grep blackarch\n\n${YELLOW}# Note - it maybe be necessary to overwrite certain packages when installing blackarch tools. If\n# you experience ${RED}'failed to commit transaction'${YELLOW} errors, use the --needed and --overwrite switches\n${YELLOW}# For example:${NC}\n${CYAN}$ sudo pacman -Syyu --needed blackarch --overwrite='*'\n"
  
  exit;

  else
    echo
    echo "Exiting..."
    exit;
  fi

else
  echo
  echo "Exiting..."
  exit;
fi