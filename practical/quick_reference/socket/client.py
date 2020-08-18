import socket
#socket.AF_INET => Using IPv4
#socket.SOCK_STREAM => Using TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#'127.0.0.1 loop back address, 12345 port number
s.connect(("127.0.0.1", 12345))

while True:
    send = "MESSAGE\n"
    s.sendall(send.encode())
    
    msg = s.recv(1024).decode()
    print(msg)
    
s.close()

