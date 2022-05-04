import psutil
import platform
from datetime import datetime
from colorama import Fore, Back, Style, init

init(autoreset=True)
yellow = Fore.YELLOW
blue = Fore.BLUE
cyan = Fore.CYAN
green = Fore.GREEN
red = Fore.RED
pink = Fore.MAGENTA
frst = Fore.RESET
white = Style.BRIGHT + Fore.WHITE
lightBlue = Fore.LIGHTBLUE_EX





def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

print(f"{white}="*40, f"{cyan}System Information{frst}", f"{white}="*40)
uname = platform.uname()
print(f"{white}System: {uname.system}")
print(f"{white}Node Name: {uname.node}")
print(f"{white}Release: {uname.release}")
print(f"{white}Version: {uname.version}")
print(f"{white}Machine: {uname.machine}")
print(f"{white}Processor: {uname.processor}")

# Boot Time
print(f"{white}="*40, f"{yellow}Boot Time{frst}", f"{white}="*40)
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
print(f"{white}Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

# let's print CPU information
print(f"{white}="*40, f"{red}CPU Info", f"{white}="*40)
# number of cores
print(f"{white}Physical cores:", psutil.cpu_count(logical=False))
print(f"{white}Total cores:", psutil.cpu_count(logical=True))
# CPU frequencies
cpufreq = psutil.cpu_freq()
print(f"{white}Max Frequency: {cpufreq.max:.2f}Mhz")
print(f"{white}Min Frequency: {cpufreq.min:.2f}Mhz")
print(f"{white}Current Frequency: {cpufreq.current:.2f}Mhz")
# CPU usage
print(f"{white}CPU Usage Per Core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"{white}Core {i}: {percentage}%")
print(f"{white}Total CPU Usage: {psutil.cpu_percent()}%")

# Memory Information
print(f"{white}="*40, f"{blue}Memory Information", f"{white}="*40)
# get the memory details
svmem = psutil.virtual_memory()
print(f"{white}Total: {get_size(svmem.total)}")
print(f"{white}Available: {get_size(svmem.available)}")
print(f"{white}Used: {get_size(svmem.used)}")
print(f"{white}Percentage: {svmem.percent}%")
print(f"{white}="*20, f"{lightBlue}SWAP", f"{white}="*20)
# get the swap memory details (if exists)
swap = psutil.swap_memory()
print(f"Total: {get_size(swap.total)}")
print(f"Free: {get_size(swap.free)}")
print(f"Used: {get_size(swap.used)}")
print(f"Percentage: {swap.percent}%")

# Disk Information
print("="*40, "Disk Information", "="*40)
print("Partitions and Usage:")
# get all disk partitions
partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"=== Device: {partition.device} ===")
    print(f"  Mountpoint: {partition.mountpoint}")
    print(f"  File system type: {partition.fstype}")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        # this can be catched due to the disk that
        # isn't ready
        continue
    print(f"  Total Size: {get_size(partition_usage.total)}")
    print(f"  Used: {get_size(partition_usage.used)}")
    print(f"  Free: {get_size(partition_usage.free)}")
    print(f"  Percentage: {partition_usage.percent}%")
# get IO statistics since boot
disk_io = psutil.disk_io_counters()
print(f"Total read: {get_size(disk_io.read_bytes)}")
print(f"Total write: {get_size(disk_io.write_bytes)}")

# Network information
print("="*40, "Network Information", "="*40)
# get all network interfaces (virtual and physical)
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        print(f"=== Interface: {interface_name} ===")
        if str(address.family) == 'AddressFamily.AF_INET':
            print(f"  IP Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast IP: {address.broadcast}")
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            print(f"  MAC Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast MAC: {address.broadcast}")
# get IO statistics since boot
net_io = psutil.net_io_counters()
print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")