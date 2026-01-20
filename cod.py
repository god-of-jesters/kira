a = input().split(';')
c = input()
s = 0
for i in a:
    if i.split('|')[2] == c:
        s += 1
print(s)