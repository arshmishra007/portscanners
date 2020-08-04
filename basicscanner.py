#!/usr/bin/python
from socket import *
from termcolor import colored

sock = socket(AF_INET,SOCK_STREAM)

setdefaulttimeout(1)

host = input("enter the host to scan")

def portscanner(port):
    if sock.connect_ex((host,port)):
       print(colored("port %d is closed"%(port),"red"))
    else:
       print(colored("port %d is open"%(port),"green"))
for port in range(1,1000)
    portscanner(port)
       
