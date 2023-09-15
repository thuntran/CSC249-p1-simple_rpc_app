#!/usr/bin/env python3

# import socket

# HOST = "127.0.0.1"  # The server's hostname or IP address
# PORT = 65432  # The port used by the server

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     s.sendall(b"Hello, world")
#     data = s.recv(1024)

# print(f"Received {data!r}")

import socket
import argparse  # Import argparse library for handling command-line arguments

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

def create_request(operation, arg1, arg2):
    return f"{operation} {arg1} {arg2}"

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description="RPC Client")

# Add arguments for operation, arg1, and arg2
parser.add_argument("operation", choices=["add", "subtract"], help="Operation to perform")
parser.add_argument("arg1", type=int, help="First argument")
parser.add_argument("arg2", type=int, help="Second argument")

# Parse the command-line arguments
args = parser.parse_args()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Connected to {HOST}:{PORT}")
    request_data = create_request(args.operation, args.arg1, args.arg2)
    s.sendall(request_data.encode())
    data = s.recv(1024)
    print(f"Received response: {data.decode()}")
