internet = {'a': [0, 1], 'b':[0, 0], 'c':[1, 1]}
n = int(input())
for i in internet:
    if internet[i].count(0) > n:
        print(i)