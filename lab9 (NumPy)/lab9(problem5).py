import numpy as np

arr = np.array([10, -5, 20, -10, 30, -2, 40])

print("Original Array:")
print(arr)


arr[arr < 0] = 0

print("\nArray after replacing negative values with 0:")
print(arr)