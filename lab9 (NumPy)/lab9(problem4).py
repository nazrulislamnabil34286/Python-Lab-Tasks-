import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([10, 25, 30, 45, 50])

matching_positions = np.where(arr1 == arr2)

print("First Array:")
print(arr1)

print("\nSecond Array:")
print(arr2)

print("\nPositions where elements match:")
print(matching_positions)