
import socket

TARGET_IP = "192.168.1.10"
TARGET_PORT = 5006

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes('Tugas 2 Program Jaringan'.encode()),(TARGET_IP,TARGET_PORT))