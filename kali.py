import os,sys

server = raw_input("Enter IP/Server:" )
port = raw_input("Port: ")

os.system("ssh root@" + server + " -p" + port)