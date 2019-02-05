import numpy as np
#add 2 matrices
a=np.ones((3,3))
b=np.ones((3,3))*3
c=a+b
print(c)
d=a-b
print(d)
e=np.matmul(a,b)
f=np.dot(a,b)
print(e)
print(f)