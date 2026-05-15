import time
import os
import sys
import shutil

# ============
# == PISTON ==
# == MODULE ==
# ============

# Info:
# v1.1
# FOSS - AGPL 3.0
# classiccatlinux (randomnerd41)

# Terms:
# I AM NOT AT FAULT
# FOR ANY HARM DONE
# TO ANY SYSTEMS!
# By using PISTON
# or a program with PISTON
# in it you agree to this.

def clear():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
        
def wait(wt):
    time.sleep(wt)
    
print("PISTON-#: The PISTON module was used in this program.")
print("https://github.com/randomnerd41/PISTON")
wait(5)
clear()

def cmd(c):
    os.system(c)

def debian_autoremove_sudo():
    if shutil.which("apt"):
        os.system("sudo apt autoremove -y")
        time.sleep(5)
    else:
        print("PISTON-#: Apt not found!")
        print("If you believe this is an error, please contact the owner of this program.")
        print("Exiting...")
        wait(5)
        clear()
                       
def update_debian_sudo():
    if shutil.which("apt"):
        os.system("sudo apt update -y && sudo apt full-upgrade -y")
        time.sleep(3)
        clear()
    else:
        print("PISTON-#: Apt not found!")
        print("If you believe this is an error, please contact the owner of this program.")
        print("Exiting...")
        wait(5)
        clear()
  
def update_debian():
    if shutil.which("apt"):
        os.system("apt update -y && apt full-upgrade -y")
        time.sleep(3)
        clear()
    else:
        print("PISTON-#: Apt not found!")
        print("If you believe this is an error, please contact the owner of this program.")
        print("Exiting...")
        wait(5)
        clear()

def update_fedora_sudo():
    if shutil.which("dnf"):
        os.system("sudo dnf update -y")
        time.sleep(3)
        clear()
    else:
        print("PISTON-#: Dnf not found!")
        print("If you believe this is an error, please contact the owner of this program.")
        print("ending the program...")
        wait(5)
        clear()
        
def update_fedora():
    if shutil.which("dnf"):
        os.system("dnf update -y")
        time.sleep(3)
        clear()
    else:
        print("PISTON-#: Dnf not found!")
        print("If you believe this is an error, please contact the owner of this program.")
        print("ending the program...")
        wait(5)
        clear()
     
def osname():
    name = sys.platform
    print("OS = ", name)
    time.sleep(3)
    clear()

ms = lambda x: time.sleep(x / 1000)
