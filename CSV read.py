import numpy as np
from matplotlib import pyplot as plt

y=np.genfromtxt('waveform.csv',delimiter=',')
m=np.mean(y)
print(m)
sd=np.std(y)
print(sd)

fig,a = plt.subplots(2,1)
a[0].plot(y)
a[0].set_title('Waveform')
a[1].hist(y, bins = [-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9])
a[1].set_title('Histogram')
plt.show() 
