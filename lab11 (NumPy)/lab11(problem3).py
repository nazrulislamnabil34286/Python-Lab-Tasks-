import numpy as np

mat = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Array:")
print(mat)

column_sum = np.sum(mat, axis=0)

row_sum = np.sum(mat, axis=1)

print("\nSum of each column:")
print(column_sum)

print("\nSum of each row:")
print(row_sum)