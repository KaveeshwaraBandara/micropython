import machine
import time

led = machine.Pin(2, machine.Pin.OUT)

counter = 0

def blink_LED_ntimes(num, t_on, t_off, msg):
    while (counter < num):
    led.on()
    time.sleep(t_on)
    led.off()
    time.sleep(t_off)
    counter+=1
    print(msg)
