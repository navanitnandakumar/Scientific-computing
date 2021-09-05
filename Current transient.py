import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

def model(i,t):
  didt = -((5*math.exp(-t))/r+(i/rc))
  return didt

t=np.linspace(0,20)
V=5
rc=3
r=3
i0=V/r
OI= odeint(model,i0,t)

plt.plot(t,OI)
plt.xlabel('time')
plt.ylabel('current')
plt.title('current transient response of RC circuit for 5e(-t)u(t)')
plt.show()
