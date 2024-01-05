import time
from machine import Pin, DAC

dac = DAC(Pin(25))
button = Pin(35, Pin.IN)

i = 0  # current time index

# max value is 255 = 3V
signal = [0, 255]
arr_len = 2

while True:
    while button.value() == 0:
        dac.write(signal[i])
        i = (i + 1) % arr_len