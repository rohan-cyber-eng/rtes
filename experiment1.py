from gpiozero import LED
from time import sleep

led1= LED(23)
led2= LED(24)
led3= LED(25)
led4= LED(1)

while True:
    led4.off()
    led1.on()
    sleep(.5)
    led1.off()
    led2.on()
    sleep(.5)
    led2.off()
    led3.on()
    sleep(.5)
    led3.off()
    led4.on()
    sleep(.5)
    led1.on()
    led2.on()
    led3.on()
    led4.on()
    sleep(.5)