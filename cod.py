a = input().split()
b = input().split()
c = input().split()
s = 0
for i in a:
    if i in b and i in c:
        s += 1
print(s)