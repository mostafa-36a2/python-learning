from io import StringIO
from datetime import timedelta
import time

# Testing string concatenation
start_time = time.time()
string = ""
for i in range(100_000):
    string += ("0123456789")
end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time for str:",timedelta(seconds=elapsed_time))

# Testing StringIO
string_io = StringIO()
start_time = time.time()
# x100 times the previews test
for i in range(10_000_000):
    string_io.write("0123456789")
end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time for StringIO:",timedelta(seconds=elapsed_time))