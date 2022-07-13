#!/usr/bin/python3 -tt
import subprocess
import os
import shutil
import content
import index


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
        print("style.css added using: "+ stylevar )

    except Exception as e:
        errsty = str("[Errno 2] No such file or directory: " + "\'"+ sFile + "\'")
        if str(e) == errsty:
            print("Anura Error: "+ stylevar + " does not exist")
            shutil.rmtree(bcx)   

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
        errcon = str("[Errno 17] File exists: "+ "\'"+ title + "\'")
        errsty = str("[Errno 2] No such file or directory: " + "\'"+ sFile + "\'")
        if str(e) == errcon:
            print("Anura Error: "+ title + " alredy exists")
        elif str(e) == errsty:
            print("Anura Error: "+ sFile + " does not exist")
create()
