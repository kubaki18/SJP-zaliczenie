import socket

HOST = "127.0.0.1"
PORT = 53029


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while command := input("$ "):
        print(command)
        s.sendall(str.encode(command))
        data = s.recv(1024)
        print(str(data, 'utf-8'))
