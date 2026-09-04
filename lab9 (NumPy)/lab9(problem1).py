import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

print("Original Array:")
print(arr)

new_shape = arr.reshape(2, 3)

print("\nReshaped Array:")
print(new_shape)