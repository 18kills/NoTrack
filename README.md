# NoTrack
Proxy loop for linux terminal writen in python and bash

Sets an http, https, and sock proxy for the terminal                      
Changes all of the proxies after an amount of time that the user sets                           
Before it connects to a proxy it first checks if it is up by scanning the ip address and the port             
If the proxy is not up then it tries the next proxy               

### How to Use
1) Setup NoTrack
2) Add more proxies to lists(Optional)
3) Enter source run.sh to start NoTrack


### How to Setup
1) Compile the setup.sh file
2) Run the setup.sh file

### How to Update Proxys
1) Go to NoTrack folder
2) Enter the proxies folder
3) This folder has three files, http.list, https.list, sock.list
4) Add proxy to corresponding file
5) Formate for proxies are host:port
