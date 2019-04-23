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

def IDFT(X):
	j = np.complex(0,1)
	x = []
	N = len(X)
	for n in range(0,N):
		y = 0
		for k in range(0,N):
			y += ( X[k] * np.exp((2*j*np.pi*k*n)/N) ) / N
		x.append(y)
	#print X
	return x

x1 = [1,2,3,4]
x2 = [1,2,3,4]

X1 = DFT(x1,4)
X2 = DFT(x2,4)

X3 = []

X3 = np.dot(X1,X2)

#X3 = IDFT(X3)

def conv(x1,x2):
	N1 = len(x1)
	N2 = len(x2)
	for i in range(N1-1,N1+N2-1):
		x1.append(0)
	for i in range(N2-1,N1+N2-1):
		x2.append(0)
	x3 = np.zeros(N1+N2)
	y = np.zeros(N1)
	for n in range(0,N1+N2-1):
		for k in range(0,N1+N2-1):
			x3[n] = x3[n] + ( x1[k] * x2[n-k])
	for i in range(0,N1):
		y[i] = x3[i] + x3[i+N1]
	return y

#x1x2 = conv(x1,x2)

#print x1x2
print X3
