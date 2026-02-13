print('\n---Temperature Checker---')

current_temp = int(input('Current Temperature in Celsius: '))

if current_temp > 30:
    print('Hot day! Stay hydrated.')

elif 10 <= current_temp <= 30:
    print('Pleasant weather!')

else:
    print('So cold right?')
