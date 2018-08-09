import socket
s=socket.socket()
#host = socket.gethostname()
s.connect(("127.0.0.1",5555))
data = s.recv(1024)
if data:
   print(data)
s.close()
