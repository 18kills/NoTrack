#!/bin/bash
while :
do
	cp ~/.bashrc.original ~/.bashrc
	./NoTrack.py
	chmod +x setProxies.sh
	./setProxies.sh
	source ~/.bashrc
	env | grep 'proxy'
	curl ipinfo.io/ip
done
