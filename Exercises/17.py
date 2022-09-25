x = str(input())
count = 1
a = 7

i = 0
while i < len(x) - 1:
    print("Cycle : ", i)
    if x[i] == x[i + 1]:
        print("Count++", i)
        count += 1
    else:
        count = 0
    i += 1

if count >= a:
    print("yes")
else:
    print("no")
