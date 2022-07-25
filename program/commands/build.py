#!/usr/bin/python3 -tt
import subprocess
import os
import shutil

def buildstyle():
    name = str(input("Name: "))
    colors = str(input("Colors (4 separated by space): "))
    modify_p = str(input("Modify features for general settings? [Y/n]"))
    
    if modify_p.lower() == "y":
        print("comming soon")
    elif modify_p.lower() == "n":
        print("Using Anura default general settings") 
    modify_c = str(input("Do you want modify components settings? [Y/n]"))
    
    if modify_c.lower() == "y":
        print("Please select what components yo want to modify (Separated by space)")
        print("If you don't know the names, press \"h\" to display it")
    elif modify_c.lower() == "n":
        print("Using Anura default in components settings")
        print("Done ;)")
