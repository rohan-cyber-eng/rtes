import BlynkLib
from BlynkTimer import BlynkTimer
import RPi.GPIO as GPIO
from sht20 import SHT20
import time



sht=SHT20(1,resolution=SHT20.TEMP_RES_14bit)


led1=23
led2=24
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

x=20

BLYNK_AUTH_TOKEN='ciP58dj5_ywq_mZMh3lRweV8m-HT-f6w'

blynk=BlynkLib.Blynk(BLYNK_AUTH_TOKEN)

timer=BlynkTimer()

@blynk.on("connected")
def blynk_connected():
    print("You Have Connected to New Blynk2.0")
    print("...........................")
    time.sleep(2);
def myData():
    humidity=sht.read_humid()
    temperature=sht.read_temp()
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature,humidity))
    else:
        print("sensor failure. check wiring");
    blynk.virtual_write(1,humidity,)
    blynk.virtual_write(0,temperature)
    print("values sent to new Blynk Server!")
timer.set_interval(2,myData)

     
     
@blynk.on("V2")
def v0_write_handler(value):
    if int(value[0]) is not 0:
        GPIO.output(led1, GPIO.HIGH)
        print('LED 1 HIGH')
        
    else:
        GPIO.output(led1, GPIO.LOW)
        print('LED 1 LOW')
        
@blynk.on("V3")
def v1_write_handler(value):
    if int(value[0]) is not 0:
        GPIO.output(led2, GPIO.HIGH)
        print('LED 4 HIGH')
        
    else:
        GPIO.output(led2, GPIO.LOW)
        print('LED 4 LOW')
        
        
@blynk.on("connected")
def blynk_connected():
    print("Raspberry Pi Connected to New Blynk")
    
while True:
    blynk.run()
    timer.run()

