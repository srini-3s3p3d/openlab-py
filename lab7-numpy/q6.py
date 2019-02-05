import numpy as np
x=np.arange(1,101)
x=x.reshape(10,10)
x=np.pad(x,pad_width=1,mode='constant',constant_values=0)
print(x)