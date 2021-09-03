import numpy as np
a = np.array([1+2j,2+3j,3+4j,4+5j,5+6j])
x = a.astype(int)
print("complex array : ",a)
print("integer array : ",x)
b = np.array([6+5j,5+4j,4+3j,3+2j,2+1j])
print("second complex array : ",b)
print("sum of arrays : ",np.multiply(a,b))
