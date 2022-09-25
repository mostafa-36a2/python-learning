s1 = input("Please enter s1: ")
s2 = input("Please enter s2: ")
s3 = input("Please enter s3: ")

if s1 + s2 == s3:
    print("s1 + s2 == s3")

if s1 == s2:
    print("s1 == s2")
elif s1 in s2:
    print("s1 in s2")

if len(s1) > len(s2):
    s4 = s1 + s2
if len(s1) < len(s2):
    s4 = s2 + s1

index_of_half = len(s1) // 2
if s2 in s1[index_of_half:]:
    print("s2 is in the second half of s1")

print("The first half of s1:", s1[:index_of_half])
