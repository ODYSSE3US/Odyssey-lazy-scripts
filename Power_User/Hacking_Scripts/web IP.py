import socket
from colorama import Fore
IP_addres = socket.gethostbyname("www.google.co.uk")
print (Fore.RED + IP_addres)
