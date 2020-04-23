import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# address = input('Enter IPv4 address of server: ')
# port = int(input('Enter port number of server: '))

address = "127.0.0.1"
port = 12345

my_socket.connect((address, port))
message=my_socket.recv(1024)
print(message.decode())
message = "Hello from client\n"
my_socket.sendall(message.encode())
my_socket.close()
