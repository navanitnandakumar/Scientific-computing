import numpy as np
x = -150
y = abs(x)
z = 1+5j
t = np.sin(np.pi/6)
N = complex(1,5)
v = [0,np.sin(np.pi/4),np.sin(np.pi/3),np.sin(np.pi/2)]
print(v)
b = np.sinc(v)
print(b)
print(np.real(z))
print(np.imag(z))
print(y)
print(t)
print(N)
