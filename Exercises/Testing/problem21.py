# a=int(input())
# b=int(input())
# c=int(input())
# if (a!=1) and (b!=1) and (c!=1):
#     print(a*b*c)
# elif (a==1 and b==1 and c==1) or (a==1 and c==1):
#     print(a+b+c)
# elif (a==1 and b==1) or (a==1):
#     print((a+b)*c)
# elif (b==1) and (c==1) or (c==1):
#     print(a*(b+c))
# elif b==1:
#     if a>c:
#         print(a*(b+c))
#     elif a<c :
#         print((a+b)*c)
#     elif a==c:
#         print((a+b)*c)

# --------------------Other way--------------------#

# a=int(input())
# b=int(input())
# c=int(input())
# if (a!=1) and (b!=1) and (c!=1):
#     print(a*b*c)
# elif a==1 and c==1:
#     print(a+b+c)
# elif a==1:
#     print((a+b)*c)
# elif c==1:
#     print(a*(b+c))
# elif b==1:
#     if a>c:
#         print(a*(b+c))
#     else :
#         print((a+b)*c)
# print("Note: Thanks to Muhammad KaraBala for his good noticing")

# --------------------Other way--------------------#

# a=int(input())
# b=int(input())
# c=int(input())
# h=a+b+c
# j=a*b*c
# k=(a+b)*c
# l=a*(b+c)
# print(max(h,j,k,l))

# --------------------Other way--------------------#

a = int(input())
b = int(input())
c = int(input())
print(max(a + b + c, a * b * c, (a + b) * c, a * (b + c)))
ac = a * c
bc = b * c
ab = a * b

a1 = a + b + c
a4 = a * b * c
a5 = ac + bc
a3 = ab + ac

a2 = a + bc  # For sure it is < a5
a6 = ab + c  # For sure it is < a3

for i in range(100):
    for j in range(100):
        for k in range(100):
            if max(a1, a4, a5, a3) < max(a2, a6):
                print(i, j, k)
            else:
                print(i, j, k, end="\r")
