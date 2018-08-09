import socket
from threading import Thread
import threading 
import time
#from pathlib2 import path
#from SocketServer import ThreadingMixIn
import os
try:
    class ClientThread(Thread):
       def __init__(self,ip,port):
          Thread.__init__(self)
          self.ip=ip
          self.port=port
          print("new thread started at: " + str(time.ctime())) #to print the time 
          print("\nThe number of active threads are: "+ str(threading.active_count())) #to print current active threads
          print("\nclient  is " + str(ip) + ":" + str(port)) #print client address (use telnet first)
          conn.send("thank you for connecting") #sending msg to connect using socket made for each client 
   
       def run(self):   #overriding this method to do what we want them to do 
         data="no data"
         while True:
          data = conn.recv(2048)
          if not data: 
            break
          print("receieved--" + str(data) + " from " + str(ip) + ":" + str(port))
          file=open("logs.txt",'a')
          file.write("receieved " + str(data) + " from " + str(ip) + ":" + str(port)+"\n")
          file.close()
          
       #def file_write():
       #   file = open("logs.txt",'a')
       #   file.write("received ") # + str(data) + " from " + str(ip) + ":" + str(port))
       #   file.close()
    ip = '127.0.0.1'    
    port = 5555
    buffer_size=20
    #log_file = Path("/root/sri_project")
    if not os.path.isfile("/root/sri_project/logs.txt"):  #change the directory according to your pc
       f =open("logs.txt","w")
   # f.write("first line is written\n")
    f.close()
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #dont change these 3 lines unless you know what you are doing declaring protocols like ipv4, tcp. reuse addr for re using port
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sock.bind((ip,port))
    threads=[]
    a=0
    while True:
      sock.listen(5)
      print("Waiting")
      (conn,(ip,port)) = sock.accept()  #accept returns 2 obj one connection socket 2nd is tuple which has client's address
      a=a+1
      print("no. of threads :" + str(a))
      newthread = ClientThread(ip,port)
      newthread.start()
      threads.append(newthread)
#    a=0
    for thread in threads:
       try:
          thread.join(1000)
          print("thank you for using the program")
       except:
          print("\nunable to join")
except KeyboardInterrupt:
    print("exiting..")
    exit()
   
