sweets = 0
stationery = 0
books = 0
drinks = 0

for count in range(0, 650):
    item = int(input('Enter the 3-digit code of the item sold: '))
    if item < 100 and item >= 0:
        sweets += 1
    elif item < 200 and item >= 100:
        stationery += 1
    elif item < 300 and item >= 200:
        books += 1
    elif item < 400 and item >= 300:
        drinks += 1

per_sweets = str((sweets / 650) * 100)
per_stationery = str((stationery / 650) * 100)
per_books = str((books / 650) * 100)
per_drinks = str((drinks / 650) * 100)

per = '%'

print('Sweets were', per_sweets + per, 'Stationery was', per_stationery + per, 'Books were', per_books + per, 'Drinks were', per_drinks + per, 'of the total sale!')