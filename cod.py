a = input().split(', ')
b = input().split(', ')
c = input().split(', ')
r = []
for i in a:
    if i in b and i in c and i not in r:
        r.append(i)

r.sort(reverse=True)

if len(r) > 0:
    print(', '.join(r))