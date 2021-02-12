country = input('Enter the country that you are visiting: (US, Europe: EU, Japan: J) ')
rate = float(input('Enter the conversion rate for Reais to the currency of visiting country: '))
reais = float(input('Enter the amount of reais that you want to convert: '))

value = rate * reais

if country == 'US':
    print('$', value)
elif country == 'EU':
    print('£', value)
elif country == 'J':
    print(value, 'Japanese Yen')
else:
    print('Invalid country!')
