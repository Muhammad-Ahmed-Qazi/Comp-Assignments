books = 0
maps = 0
mags = 0
code = 0000

while code != 9999:
    code = int(input('Enter the 4-digit code for the item: '))
    if code >= 1000 and code < 2000:
        books += 1
    elif code >= 2000 and code < 3000:
        maps += 1
    elif code >= 3000 and code < 4000:
        mags += 1

print('This much books are in stock:', books)
print('This much maps are in stock:', maps)
print('This much magazines are in stock:', mags)