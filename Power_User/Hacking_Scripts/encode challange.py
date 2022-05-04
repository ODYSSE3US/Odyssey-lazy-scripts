import os
import sys
import subprocess
from os import system, _exit as End

try:
    import colorama
except ImportError:
    ask = input("would you like to install the necessary dependencies? Y/N ")
    if ask == "Y" or "y":
        try:
            system("python3 -m pip install colorama")
        except:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])
        finally:
            import colorama
    elif ask == "N" or "n":
        system('cls' if os.name == 'nt' else 'clear')
        print("Exiting...")
        End(0)
    else:
        End(0)

import base64
import binascii
from colorama import Fore as F, Back as B, Style as S, init as colour
colour(autoreset=True)
WI = S.BRIGHT + F.WHITE
os.system('cls' if os.name == 'nt' else 'clear')


#Encode
#v = b"hello world"
v = bytes(input(WI + "Enter Message Or Code: "),encoding="utf-8")
os.system('cls' if os.name == 'nt' else 'clear')
x = binascii.hexlify(v)
y = str(x,"ascii")
t = y.encode("UTF-8")
c=base64.b64encode(t)
f=base64.b85encode(c)
output=binascii.hexlify(f).upper()

#Decode
e = binascii.unhexlify(output)
a = base64.b85decode(e)
s = base64.b64decode(c)
y = binascii.unhexlify(x)
#y = binascii.unhexlify(v)

print(f"{B.GREEN}{F.BLACK}Encoded Value: \n",WI + str(output),f"\n\n{B.RED}{F.BLACK}Decoded Value: \n",WI + str(y))