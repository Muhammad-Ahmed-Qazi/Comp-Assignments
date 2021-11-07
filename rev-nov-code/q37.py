one = 0; two = 0; three = 0; four = 0

for count in range(0, 5000):
    number = input('Enter any integer: (No decimals!) ')
    try:
        check = int(number)
        if len(number) == 1: one += 1
        elif len(number) == 2: two += 1
        elif len(number) == 3: three += 1
        elif len(number) == 4: four += 1
    except:
        print('Value rejected because it was not an integer!')

print('1-digit numbers:', one, '| 2-digit numbers:', two, '| 3-digit numbers:', three, '| 4-digit numbers:', four)
print('Percentage of numbers outside the range:', ((5000 - (one + two + three + four)) / 5000) * 100)
