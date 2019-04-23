import matplotlib.pyplot as plt
import numpy as np

n=np.linspace(0,200,200)
x=5*np.sin(2*np.pi*n)
noise=np.random.randint(-10,10,200)
x1=x+noise

fig=plt.figure()
#ax1=fig.add_subplot(4,1,1)
ax2=fig.add_subplot(2,1,1)
ax3=fig.add_subplot(2,1,2)
#ax4=fig.add_subplot(4,1,4)

#p=input("Order of system is : ")
#p=float(p)
p=20
y=np.zeros(200)

for i in range(0,200,1):
    j=i
    c=0
    while(j>=0 & c<=p-1):
        y[i]+=x1[j]
        j-=1
        c+=1
    y[i]=y[i]/p

#ax1.stem(n,x1)
ax2.stem(n,x)
ax3.stem(n,y)
#ax4.plot(n,y)
plt.show()