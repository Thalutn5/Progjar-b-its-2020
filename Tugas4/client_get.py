import socket
import sys
import base64
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port_num = 8888
server_address = ('127.0.0.1', port_num)
print("Connecting to Server: 127.0.0.1" , " Port:", port_num)
sock.connect(server_address)

try:
    filename = "note.txt"
    message = "gettingfile "+filename
    sock.send(message.encode())

    data = sock.recv(10000)
    file = open(filename,"wb")
    file.write(data)
    file.close()
    
    print("File has been Received")
finally:
    print("Closing Connection")
    sock.close()