import requests
import colorama
import ip2geotools
from colorama import *
from ip2geotools.databases.noncommercial import DbIpCity


init(autoreset=True)

FB = Fore.BLUE + Style.NORMAL # {FB}
FRR = Style.RESET_ALL + Fore.RESET + Back.RESET #{FRR}
FW = Fore.WHITE + Style.BRIGHT # {FW}
BB = Back.BLUE + Fore.BLACK # {BB}
FG = Fore.GREEN
BG = Back.GREEN + Fore.BLACK
FY = Fore.YELLOW #{FY}
FC = Fore.CYAN
FR = Fore.RED
BRR = Back.RED + Fore.BLACK
BKRE = Back.RESET
Full_Blue = Back.BLUE + Fore.BLUE




def IP_addr_Input():
    IP = input("Enter IP address Here: ")
    return IP


def Ip_lookup_complicated():
    IP = "24.48.0.1"
    IP_res = requests.get(f"http://ip-api.com/json/{IP}?fields=9676285")
    IP_cleanup = IP_res.text.translate({ord(i): None for i in '}{""'})
    IP_simplify = IP_cleanup.replace(",", "\n")
    IP_format = IP_simplify.replace(":",": ")
    print(IP_format)

def IP_lookup():
    try:
        IP = "24.48.0.1"
        response = DbIpCity.get(IP, api_key='free')
        IP_RESULTS = f"""
        {FG}Internet protocol Address:{FRR} {FY}{response.ip_address}
        {FG}City Of Origin:{FRR} {FY}{response.city}
        {FG}Country Of Origin:{FRR} {FY}{response.region}
        {FG}Country Code:{FRR} {FY}{response.country}
        {FG}Latitude:{FRR} {FY}{response.latitude}
        {FG}Longitude:{FRR} {FY}{response.longitude}
        {FG}Lat X Long:{FRR} {FY}{response.latitude}, {response.longitude}
        """
    except ip2geotools.errors.LocationError:
        print("a generic location error")

    except ip2geotools.errors.IpAddressNotFoundError:
        print("the IP address was not found")

    except ip2geotools.errors.PermissionRequiredError:
        print("problem with authentication or authorization of the request; check your permission for accessing the service")

    except ip2geotools.errors.InvalidRequestError:
        print("invalid request")

    except ip2geotools.errors.InvalidResponseError:
        print("invalid response")
    
    except ip2geotools.errors.ServiceError:
        print("response from geolocation database is invalid (not accessible, etc.)")

    except ip2geotools.errors.LimitExceededError:
        print("limits of geolocation database have been reached")

    print(IP_RESULTS)

IP_lookup()