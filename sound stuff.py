# generic imports
import pyaudio
import struct
import numpy as np
from scipy.fftpack import fft


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

while True:
    # reading from the stream
    data = stream.read(CHUNK)
    data_int = np.array(struct.unpack(str(2*CHUNK) + 'B', data), dtype='b')[::2]+127
    data_fft = fft(data_int)
    # we find the index of the max value from the data we read and find the frequency at that index from the frequency array
    max_val = np.max(data_fft)
    freq_index = np.where(data_fft == max_val)
    print(freq_range[freq_index])

# made with ❤ for project A.V.A.J