
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import signal

def DFT(x,N):
	j = np.complex(0,1)
	X = []
	N = len(x)
	for k in range(0,N):
		y = 0
		for n in range(0,N):
			y += x[n] * np.exp((-2*j*np.pi*k*n)/N)
		X.append(y)
	#print X
	return X

x1 = [1,2,3,4]
x2 = [1,2,3,4]
x3 = []
for i in range(0,len(x1)):
	y = x1[i]+x2[i]
	x3.append(y)

X1 = DFT(x1,4)
X2 = DFT(x2,4)
X3 = DFT(x3,4)

X1mag = np.abs(X1)
X2mag = np.abs(X2)
X3mag = np.abs(X3)
X1X2mag = X1mag + X2mag

plt.subplot(221)
plt.stem(X1mag)
plt.subplot(222)
plt.stem(X2mag)
plt.subplot(223)
plt.stem(X1X2mag)
plt.subplot(224)
plt.stem(X3mag)
plt.show()
