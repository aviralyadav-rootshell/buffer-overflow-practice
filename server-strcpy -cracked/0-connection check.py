import socket,sys
from time import sleep

ip ="127.0.0.1"
port=10000
s= socket.socket()
s.connect((ip,port))
while True:
   try:
       s.send("hello")
       data=s.recv(1024)
       print(data)
       sleep(5)
   except:
       print("crashed at :"+str(len(data)))
       sys.exit()
