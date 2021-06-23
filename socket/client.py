import socket

c=socket.socket()

c.connect(('localhost',9998))
print(c.recv(1024).decode())

message = input("enter your message:")
c.send(bytes(message,'utf-8'))
print("from server back to client :",c.recv(1024).decode())