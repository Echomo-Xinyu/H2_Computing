import socket
#socket.AF_INET => Using IPv4
#socket.SOCK_STREAM => Using TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#'127.0.0.1 loop back address, 12345 port number
s.connect(("127.0.0.1", 12345))
menu = ["ADD", "SUB", "MUL", "DIV", "STO", "RCL", "QUIT"]
print("Calculator Menu")
for i in range(len(menu)):
    print("{0:1}) {1:5}".format(i+1, menu[i]))
while True:
    option = int(input("Choose an option: "))
    if option <= 4:
        operand1 = input("Key in No.1 operand: ")
        operand2 = input("Key in No.2 operand: ")
        send = menu[option-1] + " " + operand1 + " " + operand2 + "\n"
    else:
        send = menu[option-1] + "\n"
    if send == "QUIT\n":
        break
    s.sendall(send.encode())
    
    msg = s.recv(1024).decode()
    print(msg)
    if len(msg)>7 and msg[:7]=="REPLACE":
        y = input(">>> Do you want to replace -> " + msg[8:] + "(Y/N)")
        if y == "Y":
            s.sendall("YES\n".encode())
        else:
            s.sendall("NO\n".encode())
        msg = s.recv(1024).decode()
        print(msg)
s.close()

