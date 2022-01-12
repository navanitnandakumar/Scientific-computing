import numpy as np
import matplotlib.pyplot as plt
import math
T=20
t = np.arange(0, 40, 0.01) # arguments: start, stop, step
n=1
y1 = ((-1)**n)*1/(2*n+1)*np.cos(2*math.pi*(2*n+1)*t/T)
n=2
y2 = ((-1)**n)*1/(2*n+1)*np.cos(2*math.pi*(2*n+1)*t/T)
n=3
y3 = ((-1)**n)*1/(2*n+1)*np.cos(2*math.pi*(2*n+1)*t/T)
y =(4/math.pi)*(1+y1+y2+y3)
fig,a = plt.subplots(4,1)
a[0].plot(t,y1)
a[0].set_title('First term')
a[1].plot(t,y2)
a[1].set_title('Second term')
a[2].plot(t,y3)
a[2].set_title('third')
a[3].plot(t,y)
a[3].set_title('y')
plt.show()
