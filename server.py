import time

import sys

import socket

import os
import subprocess

s = socket.socket()

host = "shreya-HCL-ME-Laptop"

port = 8080

s.connect(("shreya-HP-Laptop-15-da0xxx", port))

print("")

print(" Connected to server ")

command = s.recv(1024)

command = command.decode()

if command == "shutdown":

    print("")

    print("shutdown command")

    s.send("Command recieved".encode())

    subprocess.call('poweroff')


