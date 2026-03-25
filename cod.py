#1  Ответ 3 и 4 
#2  Ответ 1, 2, 3
#3  Ответ 2, 3
#4 
to_buy = 'Покупаем!'
not_to_buy = 'К сожалению, сегодня без покупок'
a = input()
b = input().split(', ')
if b[1] == a:
    print(to_buy)
else:
    print(not_to_buy)