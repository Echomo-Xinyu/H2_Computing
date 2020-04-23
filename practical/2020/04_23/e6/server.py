#Server
import socket

listen_socket = socket.socket()
listen_socket.bind(("127.0.0.1",9999))
listen_socket.listen()
active_socket, remote_addr = listen_socket.accept()
while True:
    send = input("Server>")
    active_socket.sendall(send.encode())
    if send=="quit":
        break
    print("WAITING FOR CLIENT")
    recv = active_socket.recv(1024)
    print("Client>"+recv.decode())
    if recv.decode()=="quit":
        break
active_socket.close()
listen_socket.close()