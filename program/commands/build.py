#!/usr/bin/python3 -tt
import subprocess
import os
import shutil
from termcolor import colored
from scipy.spatial import KDTree
import webcolors  #css3_hex_to_names
import matplotlib
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
    colors = str(input(f"{bcolors.BOLD}Colors (HEX, 4 separated by space): {bcolors.ENDC}"))
    synt_col = colors.split(" ")
    
    for i in synt_col:
        print("working")
        fchar = i[0]
        #add if,else to add or not sharp symbol < -- HERE
        yourstring = "#{0}".format(i) # --> Add sharp symbol to the start of the string < -- ELSE HERE
        normalized = webcolors.normalize_hex(yourstring)
        finalcol = webcolors.hex_to_name(normalized)
        fop = str(finalcol)
        print(colored(finalcol, fop))
          #  named_color = css3_hex_to_names(#fff)
        
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
            print(f"{bcolors.OKGREEN}Done ;){bcolors.ENDC}")
            y = 2 
        else:
            y = 1
# ------------------- -- -- - Build file - -- -- ---------------------------------
    

