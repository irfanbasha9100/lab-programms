
import matplotlib.pyplot as plt
import numpy as m
F=5
t=m.arange(0,1,0.01)
A=m.sin(2*m.pi*F*t)
plt.subplot(211)
plt.plot(t,A)
plt.xlabel("------>time")
plt.ylabel("------>Amplitude")
B=m.sin((2*m.pi*F*t)+90)
plt.subplot(212)
plt.plot(t,B)
plt.xlabel("------>time")
plt.ylabel("------>Amplitude")
plt.show()
