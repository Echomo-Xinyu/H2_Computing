import socket
#socket.AF_INET => Using IPv4
#socket.SOCK_STREAM => Using TCP
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#'127.0.0.1 loop back address, 2345 port number
listen_socket.bind(('127.0.0.1', 12345))
print("waiting connection...")

listen_socket.listen()
game_socket, addr = listen_socket.accept()
print("connection accepted:")

while True:
    # server always waits for client's msg
    rx_msg_str = ""
    while "\n" not in rx_msg_str:
        rx_msg_str += game_socket.recv(1024).decode()
    # operation undertake

game_socket.close()
listen_socket.close()