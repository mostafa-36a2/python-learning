import collections

import matplotlib.pyplot as plt
from main import get_list_of_numbers, shift_list_to_zero

# sample list
list_of_numbers = get_list_of_numbers()
sorted_lon = sorted(list_of_numbers)
numbers = shift_list_to_zero(sorted_lon)
print(len(numbers))
counter = dict(collections.Counter(numbers))
# numbers = [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 8, 9]
# calculate frequency of each number

# create bar plot of frequency
plt.bar(counter.keys(), counter.values())

fig, ax = plt.subplots()
ax.bar(
    counter.keys(),
    counter.values(),
    # width=max(numbers),
    log=True,
    ec="k",
    align="edge",
)
# ax.set_xscale("log")
plt.show()
