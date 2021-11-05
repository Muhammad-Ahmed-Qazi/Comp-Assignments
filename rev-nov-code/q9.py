gr_hundred = 0

for count in range(0, 50):
    number = float(input('Enter any number: '))
    if number > 100: gr_hundred = gr_hundred + 1

print('These many numbers were greater than 100:', gr_hundred)