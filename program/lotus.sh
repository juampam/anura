#!/bin/bash
PTH="$1"
PROGRAM="$0"
clear
alive=1
while [ $alive == 1 ]
do
	read -p "[$(tput setaf 2)Anura/$(tput setaf 8)$PTH$(tput sgr 0)]$ " ins
	case $ins in
		"exit")
			alive=0
		;;
		"ls")
			Pfind
		;;
		"")
		;;
	esac
done
