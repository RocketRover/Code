from gpiozero import DigitalInputDevice


def encoderValue(encoderPIN):
    sensor_reading = DigitalInputDevice(encoderPIN)
    return sensor_reading.value


'''
theinput = DigitalInputDevice(23)

while(True):
    if theinput.value:
        print("true")
    else:
        print("false")
'''