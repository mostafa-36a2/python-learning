import redis

redis_connection = redis.Redis(host="localhost", port=6379, db=1)
redis_connection.set("productName", "Smart Watch")
print(redis_connection.get("productName"))
