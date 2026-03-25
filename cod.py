#6
to_buy = 'покупаем'
not_to_buy = 'Седня без покупочек'
a = input()
b = int(input())
s = 0
for i in a.split(', '):
    s += int(i.split(': ')[1])

if b >= s:
    print(to_buy)
else:
    print(not_to_buy)