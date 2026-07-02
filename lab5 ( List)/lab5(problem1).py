
x = 'hello .py'

words = x.split()
result = []

for word in words:
    result.append(word[::-1])

print(" ".join(result))