import itertools
import time
import uuid
from itertools import permutations
from string import ascii_uppercase

import redis

# Connect to Redis server
r = redis.Redis(host="192.168.127.31", port=6379, db=0)

# Create a hash map called 'user' with key-value pairs
index = 0
from collections import defaultdict

d = defaultdict(int)
a = time.time()

for client in ["SYR01"]:
    for RP in [
        "ABCDE",
        "ABDCE",
        "ABEDC",
        "ABECD",
        "ABDCE",
        "ABCDE",
        "ABDEC",
        "ABECD",
        "ABEDC",
        "ABCED",
        "ABECD",
        "ABDCE",
        "ABDEC",
        "ACBDE",
        "ACDBE",
        "ACBED",
        "ACEBD",
        "ACDEB",
        "ACBDE",
        "ACBED",
        "ACDBE",
        "ACEBD",
        "ACEDB",
        "ACBED",
        "ACDEB",
        "ACDBE",
        "ACEBD",
        "ACEDB",
        "ACEBD",
        "ACBED",
        "ACDEB",
        "ACEDB",
        "ADBCE",
        "ADBCe",
        "ADEBC",
        "ADECB",
        "ADCBE",
        "ADCEB",
        "ADBCE",
        "ADEBC",
        "ADCEB",
        "ADCBE",
        "ADECB",
        "ADBCe",
        "ADBEc",
        "ADEBC",
        "ADECB",
        "ADCEB",
        "ADBCe",
        "ADBEC",
        "ADECB",
        "ADEBC",
        "ADCEB",
        "ADBEC",
        "ADBEc",
        "ADBCE",
        "ADCBE",
        "ADCEB",
        "ADECB",
        "ADBEC",
        "ADBEc",
        "AEBDC",
        "AECBD",
        "AEDBC",
        "AEDCB",
        "AECDB",
        "AEBDC",
        "AEDBC",
        "AECBD",
        "AEDCB",
        "AECDB",
        "AEBDC",
        "AECBD",
        "AEDBC",
        "AEDCB",
        "AECDB",
        "AEBCD",
        "AEBDC",
        "AEBCD",
        "AECBD",
        "AEDBC",
        "AEDCB",
        "AEBCD",
        "AECBD",
        "AEBDC",
        "AEDBC",
        "AEDCB",
        "AEBCD",
        "AECDB",
        "AEDCB",
        "AEDBC",
        "AECBD",
        "AECDB",
        "AEBDC",
        "AEDBC",
        "AECBD",
        "AEDCB",
        "AEBCD",
        "AECDB",
        "AEDCB",
        "AEDBC",
        "AEBCD",
        "AECBD",
        "AEDBC",
        "AECDB",
        "AEDCB",
        "AEBCD",
        "AECBD",
        "AEDBC",
        "AECDB",
        "AEDCB",
        "BACDE",
        "BACED",
        "BADCE",
        "BADEC",
        "BAECD",
        "BAEDC",
        "BACDE",
        "BADCE",
        "BADEC",
        "BACED",
        "BAECD",
        "BAEDC",
        "BACED",
        "BACDE",
        "BADCE",
        "BADEC",
        "BAECD",
        "BAEDC",
        "BADCE",
        "BACDE",
        "BADEC",
        "BAECD",
        "BAEDC",
        "BACED",
        "BADEC",
        "BAECD",
        "BAEDC",
        "BACDE",
        "BADEC",
        "BAECD",
        "BAEDC",
        "BACED",
        "BAECD",
        "BADCE",
        "BADEC",
        "BAEDC",
        "BACDE",
        "BADCE",
        "BADEC",
        "BAECD",
        "BAEDC",
        "BCEAD",
        "BCEDA",
        "BCDAE",
        "BCDEA",
        "BCEAD",
        "BCEDA",
        "BCDAE",
        "BCDEA",
        "BCEAD",
        "BCDAE",
        "BCEDA",
        "BCDEA",
        "BCEAD",
        "BCDEA",
        "BCDAE",
    ]:
        aa = time.time()
        for i in range(1000):
            res = r.hget(f"{client}_{RP}", f"innerkey_{i}")
            d[res] += 1
            index += 1
        bb = time.time()
        print(f"Time for {RP} is {bb-aa}")

b = time.time()
print(f"Time for All is {b-a} for {index} get")
input("OK?")
print(d)

# first_key = "SYR01_('A', 'B', 'C', 'D', 'E')"
# a = time.time()
# for i in range(10):
#     res = r.hget(first_key, random.choice(keys))
#     print(res)
# b = time.time()

# print(b - a)


# Get the value of a specific field in the hash map
name = r.hget("user", "name")
print(name)  # Output: b'John'


# Delete a field from the hash map
r.hdel("user", "email")

# Check if a field exists in the hash map
# exists = r.hexists("user", "email")
# print(exists)  # Output: False
