import time
from machine import Pin

led = Pin(25, Pin.OUT)
duty = 0.7
period = 10 #ms

while True:
  led.value(1)
  time.sleep_ms(int(duty*period))
  led.value(0)
  time.sleep_ms(int((1-duty)*period))