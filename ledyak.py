from gpiozero import LED
from time import sleep

led=LED(17)

while True:
    led.on()
    print("led is fuckin on")
    sleep(1)
    led.off()
    print("led is enes off")
    sleep(1)
    