# your code goes here
import math

t = int(input())
for i in range(t):
    t = int(input())
    if t < 0:
        print("invalid")
    else:
        t = math.sqrt(t)
        if abs(int(t) - t) < 0.0000001:
            print(int(t))
        else:
            print(f"{t:.6}")
