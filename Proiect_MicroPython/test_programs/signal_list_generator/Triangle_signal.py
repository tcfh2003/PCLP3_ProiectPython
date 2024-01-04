import numpy as np
import matplotlib.pyplot as plt

def seconds_to_microseconds(t):
    return t * 10**6

def microseconds_to_seconds(t):
    return t * 10**(-6)

def esp_list(np_arr):
    np_arr = (np_arr + 1) * 127.5
    np_arr = np_arr.astype(int)
    np_arr[np_arr > 255] = 255
    print(np_arr.tolist())
    print(len(np_arr))
    return np_arr.tolist()

def triangular_wave(T, Ts):
    t = np.arange(0, T, Ts)
    triangular_wave = 2 * np.abs((t / T - 0.5) % 1 - 0.5)
    return triangular_wave

Ts = microseconds_to_seconds(50)  # Intervalul de eșantionare
frequency = 100
T = 1.0 / frequency  # Perioada semnalului (1/f)
t_triangular = np.arange(0, T, Ts)

triangular_wave = triangular_wave(T, Ts)

plt.plot(t_triangular, triangular_wave)
plt.title("Semnal Triunghiular")
plt.xlabel("Timp (s)")
plt.ylabel("Amplitudine")
plt.show()
esp_list(triangular_wave)
