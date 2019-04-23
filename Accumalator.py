import matplotlib.pyplot as plt
import numpy as np

n=np.linspace(0,100,100)
x=np.sin(2*np.pi*n)

fig=plt.figure()
ax1=fig.add_subplot(3,1,1)
ax2=fig.add_subplot(3,1,2)
ax3=fig.add_subplot(3,1,3)

ax1.plot(n,x)
ax2.stem(n,x)
plt.xlabel("------>Discrete time")
plt.ylabel("------>Amplitude")

y=np.zeros(100)
for i in range(0,100):
    j=i
    while(j>=0):
        y[i]+=x[j]
        j-=1

ax3.stem(n,y)
plt.show()