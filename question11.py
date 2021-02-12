engine = float(input('Enter the size of the engine in litres: '))

if engine > 3:
    tax = 500
elif engine > 2 and engine <= 3:
    tax = 300
elif engine > 1 and engine <= 2:
    tax = 100
else:
    tax = 0

print('The tax for your car is:', tax)