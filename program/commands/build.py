#!/usr/bin/python3 -tt
import build
from subprocess import Popen
import os
import shutil
from termcolor import colored
    class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# ------------------- -- -- - Build file - -- -- ---------------------------------
def buildstyle():
    print(f"{bcolors.OKBLUE}Building a CSS style, please type:{bcolors.ENDC}")
    name = str(input(f"{bcolors.HEADER}Name: {bcolors.ENDC} "))
    colors = str(input(f"{bcolors.BOLD}Colors (HEX codes separated by space): {bcolors.ENDC}"))
    synt_col = colors.split(" #")
    zero = synt_col[0]
    ppy = zero[1:]
    x = 1
    while x == 1:
        modify_p = str(input(f"{bcolors.BOLD}Modify features for general settings? [Y/n] {bcolors.ENDC}"))
        if modify_p.lower() == "y":
            x = 2
            print("comming soon xd")
        elif modify_p.lower() == "n":
            print(f"{bcolors.WARNING}Using Anura default general settings {bcolors.ENDC}") 
            x = 2
        else:
            x = 1
    y = 1
    while y == 1:
        modify_c = str(input(f"{bcolors.BOLD}Do you want modify components settings? [Y/n] {bcolors.ENDC} "))
    
        if modify_c.lower() == "y":
            print(f"{bcolors.BOLD}Please select what components yo want to modify (Separated by space){bcolors.ENDC} ")
            print(f"{bcolors.WARNING}If you don't know the names, press \"h\" to display it{bcolors.ENDC} ")
            y = 2
        elif modify_c.lower() == "n":
            print(f"{bcolors.WARNING}Using Anura default in components settings{bcolors.ENDC} ")
            os.system('clear')
            print(f"{bcolors.OKGREEN}"+ name +" style generated\n"+ bcolors.ENDC)
            y = 2 
        else:
            y = 1
    print("Components: Default")
    print("New Classes: False")
    print("Color scheme:")
    Process=Popen('./printcolor.sh %s %s %s %s' % (str(ppy),str(synt_col[1]),str(synt_col[2]),str(synt_col[3]),), shell=True)
    print("")
    
# ------------------- -- -- - Build file - -- -- ---------------------------------
    
    #for x in synt_col:

