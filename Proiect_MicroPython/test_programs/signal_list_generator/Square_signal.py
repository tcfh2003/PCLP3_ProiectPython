import numpy as np
import matplotlib.pyplot as plt

def seconds_to_microseconds(t):
    return t *10**(6)

def microseconds_to_seconds(t):
    return t *10**(-6)

def esp_list(np_arr):
    np_arr = (np_arr + 1) * 127.5
    np_arr = np_arr.astype(int)
    np_arr[np_arr > 255] = 255
    print(np_arr.tolist())
    print(len(np_arr))
    return np_arr.tolist()

def rectangular_wave(T, Ts, duty_cycle=0.5):
    t = np.arange(0, T, Ts)
    square_wave = np.where(np.mod(t, T) < T * duty_cycle, 1, -1)
    return square_wave

Ts = microseconds_to_seconds(50)  # Intervalul de eșantionare
frequency = 100
T = 1.0 / frequency  # Perioada semnalului (1/f)
t_rectangular = np.arange(0, T, Ts)

square_wave = rectangular_wave(T, Ts)

plt.plot(t_rectangular, square_wave)
plt.title("Semnal Dreptunghiular")
plt.xlabel("Timp (s)")
plt.ylabel("Amplitudine")
plt.show()
esp_list(square_wave)
