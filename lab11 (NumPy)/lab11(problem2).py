import numpy as np

arr = np.array([10, 20, 30, 20, 40, 20, 50])

item = 20

n = 2

positions = np.where(arr == item)[0]

print("Array:")
print(arr)

print("\nPositions of", item, ":")
print(positions)

if n <= len(positions):
    print("\nIndex of", n, "nd repetition of", item, ":", positions[n - 1])
else:
    print("\nThe requested repetition does not exist.")