import matplotlib.pyplot as plt
import numpy as m
F=5
t=m.arange(0,1,0.01)
A=m.sin(2*m.pi*F*t)
plt.xlabel("------>time")
plt.ylabel("------>Amplitude")
plt.plot(t,A)