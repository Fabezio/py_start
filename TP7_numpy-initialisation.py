import numpy as np
from numpy import int8

b = np.ones((3,2), dtype=int8)
a = np.zeros((3,2), dtype=int8)
a = a.ravel()
b = b.ravel()
print(a)
print(b)
#print(type(a.size))
ab = np.concatenate((a,b), axis=0)
abSize = ab.size
#ab = ab.reshape((6, int(abSize/2)))
print(abSize)