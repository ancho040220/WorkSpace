import sys

l1 = set()
l2 = []

l3 = set()
l4 = []

a, b = map(int, sys.stdin.readline().split())

for i in range(a):
    l2.append(sys.stdin.readline().rstrip())

for i in range(b):
    l4.append(sys.stdin.readline().rstrip())

l1 = set(l2)
l3 = set(l4)

ans = []

ans = l1 & l3

print(len(ans))
print("\n".join(sorted(ans)))