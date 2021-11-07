super_1 = 0
super_2 = 0
largest = 0

for count in range(0, 5):
    price_1 = float(input('Enter price of item no.' + str(count + 1) + ' in supermarket 1: '))
    price_2 = float(input('Enter price of item no.' + str(count + 1) + ' in supermarket 2: '))
    if price_1 > price_2: super_1 += 1; diff = price_1 - price_2
    elif price_2 > price_1: super_2 += 1; diff = price_2 - price_1
    if diff > largest: largest = diff

print('Number of items more expensive in supermarket 1:', super_1)
print('Number of items more expensive in supermarket 2:', super_2)
print('Largest price difference:', largest)