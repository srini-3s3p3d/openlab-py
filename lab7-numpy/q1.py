import numpy as np
a=np.ones((2,3),dtype=int)
a[0][1]=0
x=np.count_nonzero(a)
print(a)
print(x)