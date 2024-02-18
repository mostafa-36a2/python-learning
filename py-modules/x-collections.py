from collections import Counter

a = "Hello World, This is me, mostafa, I am learning collections.Counter"
my_counter = Counter(a)
print(my_counter.most_common(1))

################################

from collections import namedtuple

Student = namedtuple("Student", ("Name", "id"))

s = Student("Mostafa", 13)
print(s, s.Name, s.id)

################################

from collections import defaultdict

d = defaultdict(list)

d["a"] = [1, 2, 3]
d["b"] = [4, 5, 6]
print(d["a"])
print(d["b"])
print(d["c"])


################################################################
from collections import deque

de: deque = deque()
de.append(1)
de.append(2)
de.appendleft(3)
de.appendleft(4)
print(list(de))  # [4, 3, 1, 2]

de.pop()
de.popleft()
print(list(de))  # [3, 1]

de.extend([0, 1, 2])  # [3, 1, 0, 1, 2]
print(de)

de.extendleft([9, 8, 7])  # [7, 8, 9, 3, 1, 0, 1, 2]
print(de)

for i in range(5):
    de.rotate(1)
    print(de)
