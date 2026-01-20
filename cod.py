s = input().split()
a = list(map(float, input().split()))
sr = sum(a)/len(a)
for i in range(len(a)):
    if a[i] > sr:
        print(s[i])