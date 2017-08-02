#!/usr/bin/python
import sys, time, os, socket, random
#Set up the lists to put the alive proxies in
http=[]
https=[]
socks=[]
#List of the proxy types
proxyTypes=['https','socks','http']
#List of proxy lists
proxyLists=[https,socks,http]
#Type is for the type of proxy ie http https socks
#proxy is the proxy in the formate 1.1.1.1:80
def getLen(Type):
	return sum(1 for line in open('proxies/'+Type+'.list'))

def proxyLoop(Type,num):
	count=0
	f=file('proxies/'+Type+'.list').read()
	for proxy in f.split():
		if count==num:
			return proxy
		else:
			count+=1

def checkProxy():
	for count in range(3):
		Type=proxyTypes[count]
		for num in range(getLen(Type)):
			proxy=proxyLoop(Type,num)
			host=proxy[0:proxy.index(':')]
			port=int(proxy[proxy.index(':')+1:])
			host=socket.gethostbyname(str(host))
			try:
				for p in range(port,port+1):
					sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
					sock.settimeout(1)
					result=sock.connect_ex((host,p))
					if result==0:
						proxyLists[count].append(proxyLoop(Type,num))
					sock.close()
			except KeyboardInterrupt:
				pass
			except socket.gaierror:
				pass
				
def setProxies():
	os.system('cp ~/.bashrc.original ~/.bashrc')
	file=open('setProxies.sh','w')
	file.write('#!/bin/bash\n')
	file.write('echo " " >> ~/.bashrc\n')
	for x in range(3):
		proxy=proxyLists[x]
		getrand=random.randrange(len(proxy))
		file.write('echo "export {}_proxy={}://{}/" >> ~/.bashrc\n'.format(proxyTypes[x],proxyTypes[x],proxy[getrand]))
	file.write('source ~/.bashrc\n')
	file.close()
def main():
	try:
		checkProxy()
		setProxies()
		os.system('chmod +x setProxies.sh')
	except KeyboardInterrupt:
		sys.exit()
	except TypeError:
		pass

main()
