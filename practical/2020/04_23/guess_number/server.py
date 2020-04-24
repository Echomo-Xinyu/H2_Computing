import socket
from random import randint

listen_socket = socket.socket()
listen_socket.bind(("127.0.0.1", 9999))
listen_socket.listen()

active_socket, remote_addr = listen_socket.accept()

trial_num, curr = 5, 1
correct_number = randint(1, 100)

while True:
    active_socket.sendall("GUESS\n".encode())
    recv = int(active_socket.recv(1024).decode())
    print(curr, recv)
    if trial_num < curr:
        send = "GAMEOVER\n"
    elif recv > correct_number:
        send = "HIGH\n"
    elif recv < correct_number:
        send = "LOW\n"
    elif recv == correct_number:
        send = "WIN\n"
    active_socket.sendall(send.encode())
    curr += 1
    if send == "WIN\n" or send=="GAMEOVER\n":
        break
    

active_socket.close()
listen_socket.close()