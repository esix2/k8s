#!/usr/bin/env python
# coding: utf-8



import socket as s
import threading
import os
from getRole import getRole

os.system("clear")

HEADER = 64
PORT = 8080
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = s.gethostbyname(s.gethostname())
SERVER = "127.0.0.2"
ADDR = (SERVER, PORT)
server = s.socket(s.AF_INET, s.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
          msg_length = int(msg_length)
          msg = conn.recv(msg_length).decode(FORMAT)
          if msg == DISCONNECT_MESSAGE:
              connected = False
          else:
            role = getRole(msg)
            print(f"[{addr}] {msg}!")
            print(f"[QUERY] {role} is {role}!")
          conn.send(role.encode(FORMAT))
          #conn.send("Message received successfully!".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")

print("[STARTING] server is starting ...")
start()

