cards = 0
sweets = 0
stationery = 0
toys = 0

for count in range(0, 280):
    item = int(input('Enter the 3-digit code of the item sold: '))
    if item < 100 and item >= 0:
        cards += 1
    elif item < 200 and item >= 100:
        sweets += 1
    elif item < 300 and item >= 200:
        stationery += 1
    elif item < 400 and item >= 300:
        toys += 1
    else:
        count = count - 1

print('Cards were', cards, ', Sweets were', sweets, ', Stationery was', stationery, ', Toys were', toys, '!')