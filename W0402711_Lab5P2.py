from gpiozero import PWMLED
from time import sleep
from math import sin
#x=True
led = PWMLED(17)
i = 0
while True:
    i=0
    while i < 1:
        i=i+.03  
        x = sin(i)
        led.value = x # off
        sleep(.25)
        i=i+.03
        x = sin(i)
        led.value = x #half brightness
        sleep(.25)
        i=i+.03
        x=sin(i)
        led.value = x # #full brightness
        sleep(.25)