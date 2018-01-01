#!/usr/bin/python
import threading
import socket
import sys
import random
from datetime import datetime
#variables
https=[]
http=[]
socks=[]
#lists
proxyTypes=['https','socks','http']
proxyLists=[https,socks,http]
#Number of threads to use. one for each list
threadNum=len(proxyLists)
#Returns the number of proxies in the list type argument
def getLen(Type):
	return len('proxies/'+Type+'.list')

def proxyLoop(Type,num):
	return open('proxies/'+Type+'.list','r').readlines()[num]

def checkProxy(Type):
	for num in range(getLen(Type)):
		proxy=proxyLoop(Type,num)
		port=int(proxy[proxy.index(':')+1:])
		host=socket.gethostbyname(str(proxy[0:proxy.index(':')]))
		try:
			sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			sock.settimeout(1)
			result=sock.connect_ex((host,port))
			if result==0:
				proxyLists[proxyTypes.index(Type)].append(proxy[0:len(proxy)-1])
			sock.close()
		except KeyboardInterrupt:
			sys.exit()
		except socket.gaierror:
			pass

def threads():
	try:
		for numThread in range(threadNum):
			threading.Thread(target=checkProxy, args=(proxyTypes[numThread],)).start()
	except KeyboardInterrupt:
		sys.exit()

def printProxyLists():
	for num in range(len(proxyLists)):
		print str(proxyTypes[num])+' '+str(proxyLists[num])+'\n'
		
def setProxies():
	file=open('setProxies.sh','w')
	file.write('#!/bin/bash\necho " " >> ~/.bashrc\n')
	for x in range(3):
		proxy=proxyLists[x]
		getrand=random.randrange(len(proxy))
		file.write('echo "export {}_proxy={}://{}/" >> ~/.bashrc\n'.format(proxyTypes[x],proxyTypes[x],proxy[getrand]))
	file.close()

def check():
	threads()
	while threading.activeCount()>1:
		pass

#t1=datetime.now()
check()
setProxies()
#print datetime.now()-t1
