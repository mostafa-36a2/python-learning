import redis

conn = redis.Redis("localhost")

data = {"Name": "Pradeep", "Company": "SCTL", "Address": "Mumbai", "Location": "RCP"}

conn.hmset("pythonDict", data)

res = conn.hgetall("pythonDict")
print(res)
print(res[bytes("Name", encoding="utf-8")])
{"Company": "SCTL", "Address": "Mumbai", "Location": "RCP", "Name": "Pradeep"}
