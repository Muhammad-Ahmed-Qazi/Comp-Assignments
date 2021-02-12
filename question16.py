tax = 0

for count in range(0, 5000):
    price = float(input('Enter the price of your house: '))
    if price > 200000:
        tax = price * 0.02
    elif price > 100000 and price <= 200000:
        tax = price * 0.015
    elif price > 50000 and price <= 100000:
        tax = price * 0.01
    else:
        tax = 0
    print('This is the amount of tax that you have to pay:', tax)