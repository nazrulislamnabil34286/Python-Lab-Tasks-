import numpy as np

arr = np.array([12, 5, 8, 1, 19, 3])

k = 3

smallest_values = np.partition(arr, k - 1)[:k]

print("Original Array:")
print(arr)

print("\n", k, "Smallest Values:")
print(np.sort(smallest_values))