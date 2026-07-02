
from collections import Counter

x = {'a': 100, 'b': 200, 'c': 300}
y = {'a': 300, 'b': 200, 'd': 400}

result = Counter(x) + Counter(y)
print(result)