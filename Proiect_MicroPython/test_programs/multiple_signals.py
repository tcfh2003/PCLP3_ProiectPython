import time
from machine import Pin, DAC

dac = DAC(Pin(25))
button = Pin(35, Pin.IN)

# Ts_min = 50 us
# jitter = 10 us
i = 0  # current time index
# max value is 255 = 3V
# signal = [0, 128, 255, 128]
signal_sin_1khz = [127, 159, 188, 214, 235, 248, 254, 252, 242, 225, 202, 174, 143, 111, 80, 52, 29, 12, 2, 0, 6, 19,
                   40, 66, 95, 127]
signal_square_1khz = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

signal_number = 0

while True:
    if signal_number == 0:
        signal = signal_sin_1khz
        arr_len = len(signal)
    elif signal_number == 1:
        signal = signal_square_1khz
        arr_len = len(signal)

    if button.value() == 1:
        time.sleep(0.5)
        signal_number = (signal_number + 1) % 2
        time.sleep(0.5)

    while button.value() == 0:
        dac.write(signal[i])

        i = (i + 1) % arr_len
        # time.sleep_us(50)

