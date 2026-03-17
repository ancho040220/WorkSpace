import sys

test = dict()
test1 = []
ans = []
a, b = map(int, sys.stdin.readline().split())

for i in range(a):
    a = sys.stdin.readline().rstrip()
    test[a] = i+1
    test1.append(a)

for j in range(b):
    b = sys.stdin.readline().rstrip()
    if b.isdigit():
        ans.append(test1[int(b)-1])
    else:
        ans.append(test[b])

print('\n'.join(map(str, ans)))