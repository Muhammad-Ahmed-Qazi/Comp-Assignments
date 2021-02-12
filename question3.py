over = 0
under = 0

for count in range(0, 5):
    number = int(input('Please enter a number of your choice: '))
    if number < 1000:
        under = under + 1
    elif number >= 1000:
        over = over + 1

print('This many numbers were 1000 or over,', over, 'and this many were under 1000,', under, '.')