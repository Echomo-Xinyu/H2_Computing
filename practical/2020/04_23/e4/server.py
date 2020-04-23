import socket

my_socket = socket.socket()
my_socket.bind(('127.0.0.1', 12345))
my_socket.listen()

while True:
    new_socket, addr = my_socket.accept()
    new_socket.sendall(b'Hello from server\n')
    new_socket.close()