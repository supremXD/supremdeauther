from colors import white, blue
import os

def installation():
    white()
    print("")
    os.system("apt install git aircrack-ng realtek-rtl8188eus-dkms realtek-rtl8723cs-dkms realtek-rtl8814au-dkms realtek-rtl88xxau-dkms -y")
    os.system("clear")
    blue()
    print("Done!!")
    exit()

installation()
