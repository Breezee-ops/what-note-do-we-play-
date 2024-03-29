# generic imports
from calendar import c
import pyaudio
import struct
import numpy as np
from matplotlib import pyplot as plt
from tkinter import TclError
from scipy.fft import fft


# constants
CHUNK = 1024 * 2             
FORMAT = pyaudio.paInt16     
CHANNELS = 1                 
RATE = 44100

# pyaudio class instance
p = pyaudio.PyAudio()

# we open a data stream to read from here
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)
# an array containing possible frequencies that we are considering from the input
freq_range = np.linspace(0, RATE, CHUNK)
freq_range_nonv = freq_range.reshape(len(freq_range), 1)
fig, ax = plt.subplots()
x = np.arange(0, 2*CHUNK, 2)
line, = ax.semilogx(freq_range, np.random.rand(CHUNK))
ax.set_ylim(0, 1)
ax.set_xlim(20, RATE/2)
fig.show()
# print("freq start")

while True:
    # reading from the stream
    data = stream.read(CHUNK)
    #data_int = np.array(struct.unpack(str(2*CHUNK) + 'B', data), dtype='b')[::2]+127 (string unpacking and wrapping in an array)
    data_int = struct.unpack(str(CHUNK) + 'h', data)
    data_fft = np.abs(fft(data_int))*2/(33000*CHUNK)
    data_fft_nonv = data_fft.reshape(len(data_fft), 1)
    max = np.amax(data_fft_nonv)
    ind = np.where(data_fft==max)
    val = freq_range[ind][0]
    #if statements galore
    if val>=1046 and val<1108:
        print('c')
    elif val>=1108 and val<1174:
        print('c#')
    elif val>=1174 and val<1244:
        print('d')
    elif val>=1244 and val<1318:
        print('d#')
    elif val>=1318 and val<1397:
        print('e')
    elif val>=1397 and val<1480:
        print('f')
    elif val>=1480 and val<1568:
        print('f#')
    elif val>=1568 and val<1661:
        print('g')
    elif val>=1661 and val<1760:
        print('g#')
    elif val>=1760 and val<1865:
        print('a')
    elif val>=1865 and val<=1975:
        print('a#')
    elif val>=1975 and val<=2093:
        print('b')
    else:
        print(' ')
    line.set_ydata(data_fft)
    fig.canvas.draw()
    fig.canvas.flush_events()
# made with ❤ for project A.V.A.J