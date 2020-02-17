import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 31000)
print(f"starting up on {server_address}")
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)

while True:
	print("waiting for a connection")
	connection, client_address = sock.accept()
	print("connection from", client_address)
	# Receive the data in small chunks and retransmit it
	data = connection.recv(100000).decode()
	fileakhir = open(data,"rb")
	isi = fileakhir.read()
	# while isi:
	connection.sendall(isi)
	# print("sending",repr(isi))
	# isi = fileakhir.read(1024)
	fileakhir.close()
# Clean up the connection 
	connection.close()
