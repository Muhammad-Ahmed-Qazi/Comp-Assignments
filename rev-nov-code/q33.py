less = 0
greater = 0
number = 1

while number > 0:
    number = float(input('Enter any positive number: (-1 to terminate input) '))
    if number > 0:
        if number > 1000: greater += 1
        elif number < 1000: less += 1
    else: break

print('This many numbers were less than 1000:', less)
print('This many numbers were greater than 1000:', greater)
