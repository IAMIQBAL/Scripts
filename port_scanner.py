import sys
import socket

ip = sys.argv[1]
open_ports = []

ports = range(1, 65535)

# Probing the open ports

def probe_port(ip, port, res=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        r = sock.connect_ex((ip, port))
        if r==0:
            res = r
        sock.close()
    except Exception as e:
        pass
    return res

for port in ports:
    sys.stdout.flush()
    response = probe_port(ip, port)
    if response == 0:
        print(port)

if open_ports:
    print("Open Ports are: ")
    print(sorted(open_ports))
else:
    print("No open ports")