tallest = 0.00
shortest = 5.00

for count in range(0, 500):
    height = float(input('Enter the height of the student in metres(m): '))
    if height > tallest:
        tallest = height
    elif height < shortest:
        shortest = height

print('This is the height of the tallest person:', tallest)
print('This is the height of the shortest person:', shortest)