from encoderSensor import encoderValue
import socket
from time import sleep
import RPi.GPIO as GPIO

encoderPIN = 23

bufferSize = 1024

# Raspberry Pi IP address and port no
ServerPort = 2222
#ServerIP = "192.168.137.160"
ServerIP = "10.42.0.1"

# creating socket 
RPIServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# listening the connection
RPIServer.bind((ServerIP,ServerPort))
print("Server is up and listening..")
# RPIServer.listen()


while True:
    cmd,address = RPIServer.recvfrom(bufferSize)
    cmd = cmd.decode("utf-8")
    print(cmd)
    print("Client Address", address[0])
    if cmd=="GO":
        result=encoderValue(encoderPIN)
        data = str(result)
        data = data.encode("utf-8")
        RPIServer.sendto(data,address)
    if cmd!="GO":
        data = "Invalid Request"
        data = data.encode("utf-8")
        RPIServer.sendto(data,address)
