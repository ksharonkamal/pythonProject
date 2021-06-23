import socket

s = socket.socket()
print("socket created")

s.bind(('localhost',9998))

s.listen(3)
print("waiting for connections...")

while True:
    c, addr = s.accept()
    print("connected with ",addr)

    c.send(bytes("welcome to have connected to the server sucessfully..!",'utf-8'))
    message = c.recv(1024).decode()
    print("received from client : ", message)
    c.send(bytes(message, 'utf-8'))

    c.close()

