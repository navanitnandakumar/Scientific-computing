import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,2*np.pi,180)
y = np.sin(x)
deriv = np.gradient(y,(2*np.pi/180))
der2 = np. gradient(deriv,(2*np.pi/180))
plt.plot(x,y,'g',label='orginal function')
plt.plot(x,deriv,'r',label='first derivative')
plt.plot(x,der2,'b',label='second derivative')
plt.legend(loc='upper left')
