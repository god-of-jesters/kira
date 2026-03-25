f = open("markets_data.csv", "r", encoding="utf-8")

cities = {}

for line in f:
    s = line.strip()
    parts = s.split(", ")

    city = parts[0]
    money = int(parts[3])

    if city in cities:
        cities[city] += money
    else:
        cities[city] = money

f.close()

max_city = ""
max_money = -1

for city in cities:
    if cities[city] > max_money:
        max_money = cities[city]
        max_city = city

print(max_city)