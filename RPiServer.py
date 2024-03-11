import socket
import time

bufferSize = 1024
msgFromServer = "menese gtten"
ServerPort = 2222
ServerIP = "192.168.137.160"
bytesToSend = msgFromServer.encode("utf-8")
RPIsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
RPIsocket.bind((ServerIP,ServerPort))
print("Server is up and listening..")
message,address = RPIsocket.recvfrom(bufferSize)
message = message.decode("utf-8")
print(message)
print("Client Address", address[0])
RPIsocket.sendto(bytesToSend,address)
