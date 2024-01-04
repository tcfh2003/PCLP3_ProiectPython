import time
from machine import Pin, DAC

dac = DAC(Pin(25))
button = Pin(35, Pin.IN)

# Ts_min = 50 us
# jitter = 10 us
i = 0  # current time index
# max value is 255 = 3V
# signal = [0, 128, 255, 128]
signal_sin_1khz = [127, 162, 194, 221, 241, 252, 254, 246, 229, 205, 174, 140, 105, 71, 42, 19, 5, 0, 4, 18, 40, 68,
                   102]
signal_square_1khz = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
signal_triangle_1khz = [0, 22, 44, 67, 89, 112, 134, 157, 179, 201, 224, 246, 240, 218, 195, 173, 150, 128, 106, 83, 61,
                        38, 16]

signal_number = 0

while True:
    if signal_number == 0:
        signal = signal_sin_1khz
        arr_len = len(signal)
    elif signal_number == 1:
        signal = signal_square_1khz
        arr_len = len(signal)
    elif signal_number == 2:
        signal = signal_triangle_1khz

    if button.value() == 1:
        time.sleep(0.5)
        signal_number = (signal_number + 1) % 3
        time.sleep(0.5)

    while button.value() == 0:
        dac.write(signal[i])
        i = (i + 1) % arr_len
        # time.sleep_us(50)

