markets = {
    'a': ['1', '2'],
    'b': ['1', '409'],
    'c': ['12', '2']
}
a = input()
c = 0
for n, i in markets.items():
    if a in i:
        c += 1
print(c)