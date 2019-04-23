
import numpy as np
import matplotlib.pyplot as plt
import math

Ep = input("Pass Band error : ")
Es = input("Stop Band error : ")

Fp = input("Pass band Fruquency : ")
Fs = input("Stop band Fruquency : ")

Ep = float(Ep)
Es = float(Es)
Fp = float(Fp)
Fs = float(Fs)

#a = ( 1 / (Ep*Ep) )
#b = a-1
#c = ( 1 / (Es*Es) )
#d = c-1
#e = b / d
#f = ( Fp / Fs )

N1 = 0.5 * math.log ( ( (1/ (Ep*Ep) -1 ) ) / ( ( 1 / (Es*Es) ) -1 ) )
N2 = math.log(Fp/Fs)

#N1 = math.log(e)
#N2 = math.log(f)

N = N1 / N2
Fc = Fp / ((1/(Ep*Ep)-1)**(1/2*N))

print math.ceil(N)
print Fc
H = []
#F = linspace(0,1000,1)
for i in range(0,5000,1):
	x = ( 1 / math.sqrt( 1 + ( (i/Fc)**(2*N) ) ) )
	H.append(x)

plt.plot(H)
plt.show()