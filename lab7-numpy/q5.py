import numpy as np

x = np.ones((10, 10))
print('before')
print(x)
x[1:-1, 1:-1] = 0
print('after')
print(x)
