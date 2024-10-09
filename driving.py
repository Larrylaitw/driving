country = input('請問你是台灣或美國人:')
age = input('輸入你的年齡: ')
age = int(age)
if country == 'Taiwan':
    if age >= 18:
        print('you can test license')
    else:
        print('You can not test')
elif country == 'US':
    if age >= 16:
        print('you can test license')
    else:
        print('You can not test')
else:
    print('Only for Taiwan and US')