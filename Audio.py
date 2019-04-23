
import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs,data = wav.read('voice.wav')
fs=np.float(fs)
print(data)
print(len(data))
t=np.arrange(0 , len(data)/fs , 1/fs)
plt.plot(t,data)
plt.show()
wav.write('low_voice.wav',0.5*fs,data)
import scipy.io.wavfile as wav
from matplotlib import pyplot as plt
fs,data=wav.read('mm.wav')
print(fs,len(data),data)
plt.plot(data)
plt.show()
