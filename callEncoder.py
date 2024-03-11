from encoderSensor import encoderValue
from time import sleep

theSeconds = 1
counter = 0
sensorPIN = 23

while(True):
    if encoderValue(23):
        counter = counter + 1
        print(counter)
        sleep(theSeconds)
        
    else:
        print(counter)
        sleep(theSeconds)
        