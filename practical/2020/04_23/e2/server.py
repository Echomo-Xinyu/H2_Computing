import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind(('127.0.0.1', 12345))
my_socket.listen()

new_socket, addr = my_socket.accept()
print('Connected to: ' + str(addr))
message='Hello from server\n'
new_socket.sendall(message.encode())
mes = new_socket.recv(1024).decode()
print(mes)
new_socket.close()

my_socket.close()


