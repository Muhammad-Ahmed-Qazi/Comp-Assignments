largest = 0

for count in range(0, 3):
    number = float(input('Enter any number: '))
    if number > largest: largest = number

print('This is the largest of the three numbers:', largest)
