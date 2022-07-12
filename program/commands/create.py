#!/usr/bin/python3 -tt
import subprocess
import os
import shutil
import content

title = "Hola"
name = str("index.html")
bcx = "Hola"
stylevar = ""

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
print(stylevar +" style added")

path = bcx +'/'+ name
bcontent = content.example()
hcontent = str("\t<title>"+title+"</title>") + content.head()
head = str("<head>\n" + hcontent + "\n</head>\n")
#componet = example()
body = str("<body>\n"+bcontent+"\n</body>")
file = open(path, "w")
file.write("<!DOCTYPE HTML>" + os.linesep)
file.write(head)
file.write(body)
file.close()
