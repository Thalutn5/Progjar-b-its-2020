import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 31000)
namafile = input("Nama file : ")
namafile = namafile.strip("\n")
print ('connecting')
sock.connect(server_address)

try:
    # Send data
    message = namafile
    print ("sending", message)
    print("ini nama file", message)
    sock.sendall(message.encode())
    # Look for the response
    while 1:
        data = sock.recv(100000)
        hasilakhir = open("finale" + message, 'a+b')
        if not data:
            hasilakhir.close()
            break
        hasilakhir.write(data)
        # print ("received", data.decode())
finally:
    print ('closing socket')
    sock.close()