# https://www.geeksforgeeks.org/queue-in-python/

from collections import deque

# Initializing a queue
q :deque = deque()

# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c')

print("Initial queue")
print(q)

while q:
    print(q.popleft())
exit()
# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)

print(q.popleft())
