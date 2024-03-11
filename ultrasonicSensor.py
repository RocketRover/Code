#for more info about DistanceSensor class, visit the following:
#https://gpiozero.readthedocs.io/en/stable/api_input.html

from gpiozero import DistanceSensor
from time import sleep

def distanceValueinCM(echoPIN, trigPIN):
    rawUltrasonic = DistanceSensor(echo=echoPIN, trigger=trigPIN)
    return (rawUltrasonic.distance)*100 #in centimeters