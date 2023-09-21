#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def perform_operation(operation, *args):
    result = 0
    if operation == "add":
        result = sum(args)
    elif operation == "subtract":
        if len(args) >= 2:  # subtraction is only valid with >= 2 numbers
            result = args[0] - sum(args[1:])
    else:
        return "Invalid operation"
    return result

print("Server starting - listening for connections at IP", HOST, "and port", PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected to {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            # Decode the received data and split it into parts
            request = data.decode().split()  # convert bytes back to string
            if len(request) < 2:  # must have at least 3 args 
                response = "Invalid request format"
            else:
                operation = request[0]
                args = [int(arg) for arg in request[1:]]
                response = str(perform_operation(operation, *args))
            print(f"Received client message: '{data!r}' [{len(data)} bytes]")
            print(f"Sending response: '{response}'")
            conn.sendall(response.encode())

print("Server is done!")
