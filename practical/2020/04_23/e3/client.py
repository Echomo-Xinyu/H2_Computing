import socket

my_socket = socket.socket()

address = "127.0.0.1"
port = 12345

my_socket.connect((address, port))
data = b''
while b'\n' not in data:
    data += my_socket.recv(1024)
print(data)
my_socket.close()