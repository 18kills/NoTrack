#!/bin/bash

timeout=45
print=false

input() {
	if [ $1 == "-P" ];then
		print=true
	elif [ $1 == "-p" ];then
		print=false
	elif [[ $1 == -t* ]];then
		timeout=${1:2}
	elif [[ $1 == help* ]];then
		echo "-P	echo proxy info when it changes"
		echo "-p	do not echo anything"
		echo "-t	change the amount of seconds it waits to change proxy again"
		echo "Example: ./run.sh -P -t30"
	fi
}

if [ -n "$1" ];then
	input $1
fi
if [ -n "$2" ];then
	input $2	
fi

while :
do
	cp ~/.bashrc.original ~/.bashrc
	./NoTrack.py
	chmod +x setProxies.sh
	./setProxies.sh
	source ~/.bashrc
	if [ $print = true ];then
		env | grep 'proxy'
		curl ipinfo.io/ip
	fi
	sleep $timeout
done
