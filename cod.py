s = input().split()
a = input().split()
sr = 0
for i in a:
    if i in s:
        sr += 1
print(sr)