def revenue(data):
    total = 0
    count = 0

    for item in data:
        parts = item.split(', ')
        date = parts[0]
        money = float(parts[1])

        month = date.split('/')[1]

        if month == '12':
            total += money
            count += 1

    return total / count