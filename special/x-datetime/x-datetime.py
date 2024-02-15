import datetime

now = datetime.datetime.utcnow()
print(now)

print(datetime.datetime.strftime(now, "%Y-%m-%d_%H-%M-%S"))


TODAY_CHECK = datetime.datetime.now()
start = datetime.datetime.strptime("26-11-2022", "%d-%m-%Y")
end = datetime.datetime.strptime("30-12-2022", "%d-%m-%Y")
print(f"Today is : {TODAY_CHECK}")
if start <= TODAY_CHECK <= end:
    print("PASS!")
else:
    print("YOU SHALL NOT PASS, FRODO.")
