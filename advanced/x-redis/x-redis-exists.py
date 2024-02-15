# 1. Connecting to Redis:

import redis

# Establishing a connection to Redis
r = redis.Redis(host="localhost", port=6379, db=0)

key_name = "cache-my-value"
if r.exists(key_name):
    value = r.get(key_name)
else:
    value = 0

print("Before set", type(value), value)

# Setting a value in Redis
r.set(key_name, int(value) + 1)

# Retrieving a value from Redis
value = r.get(key_name)
print("After set:", value)


# # Adding elements to a set
# r.sadd("myset", "value1")
# r.sadd("myset", "value2")
# r.sadd("myset", "value3")

# # Retrieving elements from a set
# elements = r.smembers("myset")
# print(elements)
