#Client
import socket

s = socket.socket()
s.connect(("127.0.0.1",9999))
while True:
    print("WAITING FOR SERVER")
    recv = s.recv(1024)
    print("Server>"+recv.decode())
    if recv.decode()=="quit":
        break
    send = input("Client>")
    s.sendall(send.encode())
    if send=="quit":
        break
s.close()