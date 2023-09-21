#!/usr/bin/env python3

import socket
import argparse  # Import argparse library for handling command-line arguments

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

def create_request(operation, *args):
    return f"{operation} {' '.join(map(str, args))}"

parser = argparse.ArgumentParser(description="RPC Client")
parser.add_argument("operation", choices=["add", "subtract"], help="Operation to perform")
parser.add_argument("args", nargs="+", type=int, help="Arguments (multiple)")

args = parser.parse_args()

print("Client starting - connecting to server at IP", HOST, "and port", PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Connected to {HOST}:{PORT}")
    request_data = create_request(args.operation, *args.args)
    # print(request_data)  # add 1 3 5
    s.sendall(request_data.encode())  # convert string to bytes
    data = s.recv(1024)

print(f"Received response: '{data.decode()}' [{len(data)} bytes]")
print("Client is done!")
