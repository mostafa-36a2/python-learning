import numpy as np

x = np.full((1, 1), "*")
# x[1:-1, 1:-1] = "."
x[1:3, 1:3] = "."
print(x)
