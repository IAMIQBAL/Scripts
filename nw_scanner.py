from scapy.all import *
import sys

interface = sys.argv[1]
ip_range = sys.argv[2]
broadcastMac = sys.argv[3]

packet = Ether(dst=broadcastMac)/ARP(pdst = ip_range) 

ans, unans = srp(packet, timeout =2, iface=interface, inter=0.1)

for send,receive in ans:
        print (receive.sprintf(r"%Ether.src% - %ARP.psrc%"))   