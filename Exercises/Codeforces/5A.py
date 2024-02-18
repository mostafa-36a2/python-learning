# A. Chat Server's Outgoing Traffic
# https://codeforces.com/problemset/problem/5/A
ADD = "Add"
REMOVE = "Remove"
SEND = "Send"
# Send a message from a person to all people, who are currently in the chat,
#               including the one, who sends the message


nbytes = 0


def main():
    global nbytes
    n = 0
    while line := input():
        if line[0] == "+":
            n += 1
        elif line[0] == "-":
            n -= 1
        else:
            l = len(line.split(":")[1])
            nbytes += l * n
            # print("sends ", nbytes)


try:
    main()
except Exception:
    print(nbytes)
