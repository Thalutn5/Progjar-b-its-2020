import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port_num = 8888
server_address = ('127.0.0.1', port_num)
print("Connecting to Server: 127.0.0.1" , " Port:", port_num)
sock.connect(server_address)

try:
    filename="text.txt"
    file = open(filename,"rb")
    content = file.read(10000)
    file.close()
    content = content.decode()
    message = "addingfile "+filename+" "+content
    sock.send(message.encode())

    data = sock.recv(10000).decode()
    print(data)

finally:
    print("Closing Connection")
    sock.close()