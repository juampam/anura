#!/usr/bin/python3 -tt
import subprocess
import os
import shutil
import content
import index
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

def create():
    try:
        stylevar = index.getStyle()
        title = str(index.getTitle())
        name = str("index.html")
        bcx = title


        if stylevar == "":
            stylevar = "example.css"

        sFile = "styles/"+ stylevar
        os.mkdir(bcx)
        tFile = bcx + '/'+ 'style.css'
        fileHandle = open(sFile, "r")
        texts = fileHandle.readlines()
        fileHandle.close()
        fileHandle = open(tFile, "w")

        for s in texts:
            fileHandle.write(s)

        fileHandle.close()
        print(bcolors.OKCYAN + title +" created using the style: "+ stylevar + bcolors.ENDC)

    except Exception as e:
        errsty = str("[Errno 2] No such file or directory: " + "\'"+ sFile + "\'")
        if str(e) == errsty:
            print(bcolors.WARNING + stylevar + " style does not exist" + bcolors.ENDC )
            shutil.rmtree(bcx)   
            exit()
    try:

        path = bcx +'/'+ name
        bcontent = content.example()
        hcontent = content.head()
        head = str("<head>\n" + hcontent + "\n</head>\n")
        #componet = example()
        body = str("<body>\n"+bcontent+"\n</body>")
        file = open(path, "w")
        file.write("<!DOCTYPE HTML>" + os.linesep)
        file.write(head)
        file.write(body)
        file.close()

    except Exception as e:
        print(e)
        errcon = str("[Errno 17] File exists: "+ "\'"+ title + "\'")
        errsty = str("[Errno 2] No such file or directory: " + "\'"+ sFile + "\'")
        errhtml = str("[Errno 2] No such file or directory: " + "\'"+ sFile + "\'")
        if str(e) == errcon:
            print("Anura Error: "+ title + " alredy exists")
        elif str(e) == errsty or str(e) == errhtml: 
            print("Anura Error: "+ sFile + " does not exist")
    
    # ADDING THE PROJECT TU PROJECT HISTORY FILE
    

create()
