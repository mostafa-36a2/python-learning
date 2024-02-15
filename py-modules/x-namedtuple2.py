from collections import namedtuple

BkpTuple = namedtuple("BkpTuple", ["a", "b"])
bkp_tuple = BkpTuple("hello", "yellow")
print(*bkp_tuple)
