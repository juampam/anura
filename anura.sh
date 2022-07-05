#!/bin/bash

ans="$1"
export ans

cat << EOF > pyscript.py
#!/usr/bin/python3 -tt
import subprocess
import os

if "$ans" == "":
	print("No valid arguments, try anura -h for help")
if "$ans" == "create":
	f = open("demofile2.txt", "a")
	f.write("We are progressing!")
	f.close()
if "$ans" == "-h" or "$ans" == "-help" or "$ans" == "help":
	print("Anura 1.0.2 Help Guide:\n\n New project ------------------ create")
	
EOF
					

chmod 770 pyscript.py

./pyscript.py

exit 0
