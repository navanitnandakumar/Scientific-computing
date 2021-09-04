from scipy.integrate import quad
from scipy.integrate import simps
from numpy import trapz
import numpy as np
def function(x):
 return 4*x**2+3
x = np.arange(-2,2,0.1)
y = function(x)
print (x)
print (y)
print( "area: ", 4.0*(1.0/ 3.0) * ( x[len(x)-1]**3 - x[0]**3+3*((x[len(x)-1]-x[0]))))
# using Trapezoidal rule:
area1 = trapz(y,x)
print ('area by trapizodial method: ',area1)
# using Simpson's rule:
area2 = simps(y,x)
print ('area by simpsons rule: ',area2)
area4=quad(lambda x:y,-2,2)
print("area =",area4)
