from colors import red, white, blue

import os, sys, time


if os.geteuid() != 0:
    red()
    print('This scrips needs to ve executed with root privileges. Try "sudo python3 networkrestart.py"')
    sys.exit(1)


def NetworkRestart():
    red()
    print("")
    print("IMPORTANT: DON'T GO AHEAD IF YOUR NETWORK ITS ALREADDY GOOD OR YOUR INTERFACE ITS ALREADY IN MANAGED MODE")
    print("")
    time.sleep(2)
    confirmation = input("Do you want to continue? (y/n) ----> ")
    white()
    if confirmation == "y":
        wlan = input("Name of your wifi adapter (Ex: wlan0) here ----> ")
        os.system("airmon-ng stop "+wlan+"")
        os.system("systemctl restart NetworkManager.service")
        os.system("ifdown -a")
        os.system("ifup -a")
        os.system("clear")
        blue()
        print("Goodbye :D")
        exit()
    if confirmation == "n":
        exit()


NetworkRestart()