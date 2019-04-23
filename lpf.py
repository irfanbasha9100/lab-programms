import numpy as np
import matplotlib.pyplot as plt
import cmath as cm

w=input("enter cut-off frequency: ")
n=np.linspace(-1000,1000,1000)

y=np.sin(w*n)/(np.pi*n)
def dtft(x):
	t = np.linspace(0, 1, 500)
	N=1000
	w=np.linspace(-np.pi,np.pi,N)
	x=[6,4]
	j=cm.sqrt(-1)
	y=[]
	for i in range(0,N):
	    sum=0
	    for p in range(0,len(x)):
		  #print(len(x))
		  sum=sum+(x[p]*np.exp(-j*w[i]*p))
	    y.append(sum)
	return y

Y=dtft(y)
plt.subplot(2,1,1)
plt.stem(n,y)
plt.subplot(2,1,2)
plt.plot(np.abs(Y))
plt.show()



