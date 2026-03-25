#5 
a = input()
c = 0
while a != 'конец':
    b = a.split(', ')
    if b[1] == 'посетила':
        c += 1
    a = input()
print(c)
