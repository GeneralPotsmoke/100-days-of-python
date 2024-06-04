import numpy as np

arr = np.random.rand(3, 3)
print("Array:
", arr)

mean = np.mean(arr)
print("Mean:", mean)

sum_axis0 = np.sum(arr, axis=0)
print("Sum along axis 0:", sum_axis0)
