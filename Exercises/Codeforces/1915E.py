# E. Romantic Glasses
# https://codeforces.com/contest/1915/problem/E
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    # Each a[i] has units of juice in it
    # She drinks odd, He drinks even
