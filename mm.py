import scipy.io.wavfile as wav
from matplotlib import pyplot as plt
fs,data=wav.read('mm.wav')
print(fs,len(data),data)
plt.plot(data)
plt.show()
