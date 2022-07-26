#!/bin/bash

ans="$1"
export ans
case $ans in
        "create")
               cat << EOF > commands/index.py
#!/usr/bin/python3 -tt

def getTitle():
	title = "$2"
	return title
def getStyle():
	style = "$3"
	return style

EOF
chmod 770 commands/index.py
chmod 770 commands/create.py
./commands/index.py
./commands/create.py
exit 0
mv "$2" folder
                ;;
        "help")
                cat help
                ;;
	"rename")
		mv $2 $3
		;;
	"build")
		cat << EOF > commands/exc.py
#!/usr/bin/python3 -tt
import build
build.buildstyle()
EOF
chmod 770 commands/exc.py
./commands/exc.py
		;;
	"")
		echo "No arguments, type 'anura help' to view commands information"
		;;
	*)
		echo "$ans is not a anura command"
esac
