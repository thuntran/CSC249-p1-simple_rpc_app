#!/usr/bin/env python3

# import socket

# HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
# PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print(f"Connected by {addr}")
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             conn.sendall(data)

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def perform_operation(operation, arg1, arg2):
    if operation == "add":
        return arg1 + arg2
    elif operation == "subtract":
        return arg1 - arg2
    else:
        return "Invalid operation"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server is listening on {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            # Decode the received data and split it into parts
            request = data.decode().split()
            if len(request) != 3:
                response = "Invalid request format"
            else:
                operation, arg1, arg2 = request
                try:
                    arg1 = int(arg1)
                    arg2 = int(arg2)
                    response = str(perform_operation(operation, arg1, arg2))
                except ValueError:
                    response = "Invalid argument(s)"
            conn.sendall(response.encode())

