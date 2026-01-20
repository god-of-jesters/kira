s = input()
l = []
while s != 'END':
    num = int(s.split(':')[1])
    if num > 500:
        l.append(s.split(':')[0])
    s = input()
print(l)