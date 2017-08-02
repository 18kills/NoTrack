#!/bin/bash
while :
do
	#echo Running test2.py
	./NoTrack.py
	#echo test2.py finished
	#echo Source setProxies.sh
	source setProxies.sh
	#env | grep 'proxy'
	#sleep 5
done
