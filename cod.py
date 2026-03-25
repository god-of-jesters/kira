x = int(input())

f = open("markets_data.csv", "r", encoding="utf-8")

for line in f:
    s = line.strip()
    parts = s.split(", ")

    city = parts[0]
    money = int(parts[3])

    if city == "Москва" and money > x:
        print(s)

f.close()