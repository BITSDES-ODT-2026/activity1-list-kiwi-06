#Create any list
from machine import Pin
import time

num = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

#first i = [1,0,0,0] , i[0]
led1 = Pin(4,Pin.OUT)
led2 = Pin(14,Pin.OUT)
led3 = Pin(26,Pin.OUT)
led4 = Pin(33,Pin.OUT)

while True:
    for i in num:
        led1.value(i[0]) 
        led2.value(i[1])
        led3.value(i[2])
        led4.value(i[3])
        time.sleep(0.5)
    
    #this is a shorter version of the led1.value(1), led2.value(0)etc code
