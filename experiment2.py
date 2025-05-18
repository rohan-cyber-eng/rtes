from gpiozero import Button
from gpiozero import LED
from time import sleep

led1=LED(23)
button1=Button(4, None, True)

button2 = Button(17, None, True)
while True:
    if button1.is_pressed:
        print("Button1 is pressed")
        led1.on()
            
    elif button2.is_pressed:
        print("Button1 is pressed")
        led1.off()
            
