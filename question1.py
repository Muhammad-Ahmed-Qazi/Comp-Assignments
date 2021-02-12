larg_pos = 0
larg_neg = 0

for count in range(0,5000):
    number = int(input('Please enter any positive or negative number you want: '))
    if number > larg_pos:
        larg_pos = number
    elif number < larg_neg:
        larg_neg = number
    
print('This is the largest positive number:', larg_pos)
print('This is the largest negative number:', larg_neg)