# NoTrack
Proxy loop for linux terminal written in python and bash

Sets an HTTP, HTTPS, and sock proxy for the terminal             
Changes all of the proxies after the user set wait time is finished               
Before connecting to a proxy NoTrack first checks if the proxy       
To check if the proxy is up NoTrack checks to see if the connecting port is open             
If the proxy is not open NoTrack does not add the proxy to the in program list          
NoTrack then only uses the proxies that's connecting port was open    

### How To Use
1. Setup NoTrack
2. Add more proxies to lists(Optional)
3. Enter source run.sh to start NoTrack     
   Ex: `source run.sh`       

### How to Setup
1. Compile the setup.sh file         
   Ex: `chmod +x setup.sh`
2. Run the setup.sh file as sudo       
   Ex: `sudo bash setup.sh`

### How to Update Proxys
1. Go to NoTrack folder        
   Ex: `cd NoTrack`
2. Enter the proxies folder         
   Ex: `cd proxies`
3. This folder has three files, http.list, https.list, sock.list
4. Add proxy to corresponding file
5. Format for proxies are host:port
