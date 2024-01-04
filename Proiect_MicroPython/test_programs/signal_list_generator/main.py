import numpy as np
import matplotlib.pyplot as mplot









def seconds_to_microseconds(t):
    return t * 10**6


def microseconds_to_seconds(t):
    return t * 10**(-6)


def esp_list(np_arr):
    np_arr = (np_arr + 1) * 127.5
    np_arr = np_arr.astype(int)
    for i in range(len(np_arr)):
        if np_arr[i] > 255:
            np_arr[i] = 255

    print(np_arr.tolist())
    print(len(np_arr))
    return np_arr.tolist()


Ts = microseconds_to_seconds(40)    #s
f = 1000                            #Hz
T = 1.0/f                           #s
t = np.arange(0, T, Ts)

x_sin = np.sin(2*np.pi*f*t)

mplot.plot(t, x_sin)
mplot.show()

esp_list(x_sin)
