# https://www.geeksforgeeks.org/get-current-timestamp-using-python/

# using datetime module
import datetime

# ct stores current time
ct = datetime.datetime.now()
sct = ct.strftime("%H:%M:%S.%f")
print("current time:-", sct)
