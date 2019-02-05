import numpy as np
import pprint as pp
a=np.array([[1,2,3],[4,5,6]])
print(a)
b=a.reshape(3,2)
print(b)

c=np.arange(20,100)
print(c)
d=c.reshape(4,2,10)
print(d)
print(d.flags)
print(b.itemsize)