import numpy as np
import matplotlib.pyplot as mplot

class Signal:
    def __init__(self, t, npArray):
        self.t = t
        self.npArray = npArray

    def esp_list(self):
        #np_arr = (np_arr + 1) * 127.5
        np_arr = self.npArray * 255
        np_arr = np_arr.astype(int)
        for i in range(len(np_arr)):
            if np_arr[i] > 255:
                np_arr[i] = 255

        print(np_arr.tolist())
        print(len(np_arr))
        return np_arr.tolist()


def rectangular_wave(T, Ts, duty_cycle=0.5):
    t = np.arange(0, T, Ts)
    x_square = np.where(np.mod(t, T) < T * duty_cycle, 1, -1)
    return Signal(t, x_square)


def triangular_wave(T, Ts):
    t = np.arange(0, T, Ts)
    x_triangle = 2 * np.abs((t / T - 0.5) % 1 - 0.5)
    return Signal(t, x_triangle)


def sinusoidal_wave(T, Ts):
    t = np.arange(0, T, Ts)
    x_sin = 0.5 * np.sin(2 * np.pi * f * t) + 0.5
    return Signal(t, x_sin)




def seconds_to_microseconds(t):
    return t * 10**6


def microseconds_to_seconds(t):
    return t * 10**(-6)


Ts = microseconds_to_seconds(40)    #s
f = 1000                            #Hz
T = 1.0/f                           #s

sinSignal = sinusoidal_wave(T, Ts)
squareSignal = rectangular_wave(T, Ts)
triangleSignal = triangular_wave(T, Ts)

mplot.plot(sinSignal.t, sinSignal.npArray)
mplot.show()
sinSignal.esp_list()
mplot.plot(squareSignal.t, squareSignal.npArray)
mplot.show()
squareSignal.esp_list()
mplot.plot(triangleSignal.t, triangleSignal.npArray)
mplot.show()
triangleSignal.esp_list()