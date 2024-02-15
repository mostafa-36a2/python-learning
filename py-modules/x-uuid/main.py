import uuid

print(str(uuid.uuid1()).replace("-", "")[::4])
