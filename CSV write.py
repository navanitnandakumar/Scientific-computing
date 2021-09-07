import numpy as np
from matplotlib import pyplot as plt
t = np.arange(0, 0.002, 0.00002)
f=1000
y = 2+5*np.sin(2*np.pi*f*t)
plt.plot(t,y)
plt.show()
np.savetxt('waveform.csv', y, delimiter=',')
