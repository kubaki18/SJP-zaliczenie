import socket

import handler 


HOST = "127.0.0.1"
PORT = 53029


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    handler.initialize_server()
    while True:
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f'Client connected: {addr}')
            handler.add_log(addr)
            eof = False
            while not eof:
                data = conn.recv(1024)
                data_utf = str(data, 'utf-8')
                print(data_utf)
                if not data or (data_utf.lower() in ["quit", "exit", "q"]):
                    print("Quitting...")
                    eof = True
                response = handler.handle_command(data_utf)
                conn.sendall(str.encode(response))
