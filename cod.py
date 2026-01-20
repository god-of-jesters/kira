fd = ['22', '23', '24', '25', '27']

just_mir = 'Это обычная карта МИР'
no_card = 'Карты мир не бывают с таким большим номером'
visa_mastercard = 'Возможно, это VISA или MasterCard'

i = input()

if i[:2] in fd and len(i) == 16:
    print(just_mir)
elif len(i) > 16:
    print(no_card)
else:
    print(visa_mastercard)