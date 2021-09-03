import time as tm
import numpy as np
n_tic = tm.process_time()
v1 = np.arange(0,1000000)
v2 = np.arange(0,1000000)

#loop method -->
v3 = np.zeros(1000000)
for i in range(len(v2)):
    v3[i] = v1[i] + v2[i]
print(v3)
n_toc1 = tm.process_time()

#vectorized computing method -->
v4 = v1 + v2
print(v4)
n_toc2 = tm.process_time()
print("Time for loop method = "+str(1000*(n_toc1-n_tic))+" ms")
print("Time for vectorized computing method = "+str(1000*(n_toc2-n_toc1))+" ms")
