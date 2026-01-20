a = input().split(', ')
b = input().split(', ')
c = input().split(', ')
s = 0
for i in c:
    if i in a or i in b:
        s += 1
print(s)