from ultrasonicSensor import distanceValueinCM
from time import sleep

echo_pin = 23
trig_pin = 24

while True:
    print("Distance in cm: {:.2f}".format(distanceValueinCM(echo_pin, trig_pin)))
    sleep(0.25)