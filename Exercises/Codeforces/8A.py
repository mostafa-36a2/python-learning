path = input()
left = input()
right = input()

forward = False
backward = False
both = False
fantasy = False

if left in path and right in path:
    if path.find(left) + len(left) <= path.rfind(right):
        forward = True
    if path.find(left) + len(left) <= path.find(right):
        forward = True
    if path.rfind(left) + len(left) <= path.find(right):
        forward = True
    if path.rfind(left) + len(left) <= path.rfind(right):
        forward = True

path = path[::-1]
# left = left[::-1]
# right = right[::-1]

# print(f"New path: {path}")
# print(f"New left: {left}")
# print(f"New right: {right}")

if left in path and right in path:
    if path.find(left) + len(left) <= path.rfind(right):
        backward = True
    if path.find(left) + len(left) <= path.find(right):
        backward = True
    if path.rfind(left) + len(left) <= path.find(right):
        backward = True
    if path.rfind(left) + len(left) <= path.rfind(right):
        backward = True

if forward and backward:
    print("both")
elif forward:
    print("forward")
elif backward:
    print("backward")
else:
    print("fantasy")

# print(forward)
# print(backward)
# print(both)
# print(fantasy)

# if left not in path or right not in path
