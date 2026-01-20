s = input()
l = {}
m = 0
g = ''
while s != 'END':
    gr = s.split(', ')[0]
    if gr not in l:
        l[gr] = 0
    date = s.split(', ')[1]
    if date.split('.')[-1] == '2023':
        l[gr] += 1
    s = input()
for i in l:
    if l[i] > m:
        m = l[i]
        g = i
print(g, m)