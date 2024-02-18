# Non pythonic
l = [1,2,4,7,5,1,8,6,4,9,2,3,5]

flag = False

while l:
    if l[-1] == 7:
        flag = True
        break
    print(l.pop())
    
if flag:
    print(f"pop all until 7 done: l = {l}")


# Pythonic
l = [1,2,4,7,5,1,8,6,4,9,2,3,5]

while l:
    if l[-1] == 7:
        break
    print(l.pop())
else:
    q = print(f"pop all until 7 done: l = {l}")

