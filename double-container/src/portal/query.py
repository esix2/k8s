#!/usr/bin/env python
# coding: utf-8



import socket as s



class query():
  def __init__(self):
    self.HEADER = 64
    self.PORT = 8080
    self.FORMAT = 'utf-8'
    self.DISCONNECT_MESSAGE = "!DISCONNECT"
    #self.SERVER = "127.0.1.1"
    self.SERVER = "127.0.0.2"
    self.ADDR = (self.SERVER, self.PORT)

    self.client = s.socket(s.AF_INET, s.SOCK_STREAM)
    self.client.connect(self.ADDR)

  def get_query(self, msg):
    message = msg.encode(self.FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(self.FORMAT)
    send_length += b' ' * (self.HEADER - len(send_length))
    self.client.send(send_length)
    self.client.send(message)
    if msg != self.DISCONNECT_MESSAGE:
      role = self.client.recv(128).decode(self.FORMAT)
      return role
    else:
      print("Disconnected from the server!")

  def disconnect(self):
    self.get_query(self.DISCONNECT_MESSAGE)
