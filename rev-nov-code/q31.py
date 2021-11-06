int_count = 0

for count in range(0, 1000):
    number = input('Enter any number: ')
    if '.' not in number: int_count += 1

print('These many numbers were whole numbers:', int_count)