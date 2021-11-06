highest = 0
total = 0
number = 0
count = 1

while number != -1:
    number = int(input('Enter any positive integer: (-1 to end the program) '))
    if number == -1: break
    if number > 0:
        total += number
        count += 1
        if number > highest: highest = number
    else: print('Enter only positive numbers!')

print('Average value of the input numbers:', total/count)
print('Value of largest number input:', highest)