import numpy as np
import matplotlib.pyplot as plt
from numpy import random

M = 15
x = np.arange(0, M, 1)
y = random.randint(11, size=(M))

fig,a = plt.subplots(3,1)
a[0].plot(x,y)
a[0].set_title('Line plot')
a[1].stem(x,y)
a[1].set_title('Stem plot')
a[2].bar(x,y)
a[2].set_title('Bar plot')
plt.show()
