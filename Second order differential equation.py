import numpy as np
import math
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def dx_dt(U, t):
 return [U[1], -2*U[1] - 2*U[0] + math.exp(-t)]

x0 = [0, 0] 
ts = np.linspace(0, 10, 100)
Us = odeint(dx_dt, x0, ts)
xs = Us[:,0]

plt.xlabel("t")
plt.ylabel("x")
plt.title("solution for second order ode")
plt.plot(ts,xs)
