import socket,sys
from time import sleep

ip ="127.0.0.1"
port=10000
s= socket.socket()
s.connect((ip,port))
c=0
while True:
   try:  
       buffer = "A"*30
       c=c+1
       buffer=buffer*c+"\r\n\r\n"
       s.send(buffer)
       data=s.recv(1024)
       print(data)
       sleep(2)
   except:
       print("crashed at :"+str(len(buffer)))
       sys.exit()
       
#### Result :: crashed at , 274 bytes
