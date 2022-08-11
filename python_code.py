import numpy as np


arr=np.arange(12)

reshaped=np.copy(arr)

reshaped=np.reshape(reshaped,(2,3,2))

print(repr(reshaped))
