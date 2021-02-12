sweets = 0
mags = 0
drinks = 0
code = 0000

while code != 9999:
    code = int(input('Enter the 4-digit code for the item: '))
    if code >= 1000 and code < 2000:
        sweets += 1
    elif code >= 2000 and code < 3000:
        mags += 1
    elif code >= 3000 and code < 4000:
        drinks += 1

print('This much sweets were sold:', sweets)
print('This much magazines were sold:', mags)
print('This much drinks were sold:', drinks)