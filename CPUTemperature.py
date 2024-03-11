from gpiozero import CPUTemperature
from time import sleep

while True:
    theCPUtemp = CPUTemperature()
    print(theCPUtemp.temperature)
    sleep(1)