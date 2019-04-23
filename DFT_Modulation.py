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

l = input('Delay : ')
x1 = [1,2,3,4]

def DFT_1(x,N):
	j = np.complex(0,1)
	X = []
	N = len(x)
	for k in range(0,N):
		y = 0
		for n in range(0,N):
			y +=  x[n] * np.exp((-2*j*np.pi*(k+l)*n)/N) 
		X.append(y)
	#print X
	return X


#for i in range(0,len(x1)):

X1 = DFT(x1,4)
X2 = DFT_1(x1,4)

X1mag = np.abs(X1)
X2mag = np.abs(X2)

X1phase = np.angle(X1)
X2phase = np.angle(X2)

plt.subplot(221)
plt.stem(X1mag)
plt.subplot(222)
plt.stem(X2mag)
plt.subplot(223)
plt.stem(X1phase)
plt.subplot(224)
plt.stem(X2phase)
plt.show()


