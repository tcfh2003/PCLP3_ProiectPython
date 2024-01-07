import numpy as np
import matplotlib.pyplot as mplot


class Signal:
    def __init__(self, t, npArray):
        self.t = t
        self.npArray = npArray

    def esp_list(self):
        np_arr = self.npArray * 255
        np_arr = np_arr.astype(int)
        for i in range(len(np_arr)):
            if np_arr[i] > 255:
                np_arr[i] = 255

        print(np_arr.tolist())
        print(len(np_arr))
        return np_arr.tolist()

    def plot_timedomain(self):
        mplot.plot(self.t, self.npArray)
        mplot.xlabel('t [s]')

    def plot_FFT(self):
        Ts = self.t[1] - self.t[0]
        T = self.t[-1] + Ts
        npArray_10periods = np.tile(self.npArray, 10)
        fft = np.fft.fft(npArray_10periods, 2048)
        fft = Ts/(10*T) * np.abs(fft)
        freq = np.fft.fftfreq(2048, Ts)
        mplot.plot(freq, fft)
        mplot.xlabel('f [Hz]')
        mplot.ylabel('|X(f)|')
        mplot.xlim((-(1/T) * 7 , (1/T) * 7))    #include 7 harmonics in plot


def rectangular_wave(T, Ts, duty_cycle=0.5):
    t = np.arange(0, T, Ts)
    x_square = np.where(np.mod(t, T) < T * duty_cycle, 1, 0)
    return Signal(t, x_square)


def triangular_wave(T, Ts):
    t = np.arange(0, T, Ts)
    x_triangle = 2 * np.abs((t / T - 0.5) % 1 - 0.5)
    return Signal(t, x_triangle)


def sinusoidal_wave(T, Ts):
    t = np.arange(0, T, Ts)
    x_sin = 0.5 * np.sin(2 * np.pi * f * t) + 0.5
    return Signal(t, x_sin)


def sawtooth_wave(t, Ts):
    t = np.arange(0, T, Ts)
    x_sawtooth = np.linspace(0, 1, len(t))
    return Signal(t, x_sawtooth)


def seconds_to_microseconds(t):
    return t * 10**6


def microseconds_to_seconds(t):
    return t * 10**(-6)


Ts = microseconds_to_seconds(44)    #s
f = 1000                            #Hz
T = 1.0/f                           #s

sinSignal = sinusoidal_wave(T, Ts)
squareSignal = rectangular_wave(T, Ts)
triangleSignal = triangular_wave(T, Ts)
sawtoothSignal = sawtooth_wave(T, Ts)

sinSignal.plot_timedomain()
mplot.title("Sine wave")
mplot.show()
sinSignal.plot_FFT()
mplot.title("FFT of sine wave")
mplot.show()
print("Sine wave:")
sinSignal.esp_list()

squareSignal.plot_timedomain()
mplot.title("Square wave")
mplot.show()
squareSignal.plot_FFT()
mplot.title("FFT of square wave")
mplot.show()
print("Square wave:")
squareSignal.esp_list()

triangleSignal.plot_timedomain()
mplot.title("Triangle wave")
mplot.show()
triangleSignal.plot_FFT()
mplot.title("FFT of triangle wave")
mplot.show()
print("Triangle wave:")
triangleSignal.esp_list()

sawtoothSignal.plot_timedomain()
mplot.title("Sawtooth wave")
mplot.show()
sawtoothSignal.plot_FFT()
mplot.title("FFT of sawtooth wave")
mplot.show()
print("Sawtooth wave:")
sawtoothSignal.esp_list()