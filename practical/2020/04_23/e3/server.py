import socket
import time

my_socket = socket.socket()
my_socket.bind(('127.0.0.1', 12345))
my_socket.listen()

new_socket, addr = my_socket.accept()
new_socket.sendall(b'Hello fr')
time.sleep(0.1)
new_socket.sendall(b'om server\n')
new_socket.close()
my_socket.close()