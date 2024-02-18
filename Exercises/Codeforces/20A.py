s = input()
for i in range(1, 101):
    s = s.replace("//", "/")
if s[-1] == "/" and s != "/":
    s = s[:-1]
print(s)
