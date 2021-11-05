count = 0; cd = 0; dvd = 0; video = 0; book = 0

while count < 5000:
    code = input('Enter the 5-digit code for item no.' + str(count + 1) + ': (E.g. 12345) ')
    if len(code) > 5 or len(code) < 5: 
        print('Code is invalid!')
        count = count - 1
    else:
        item_id = int(code[0])
        print(item_id)
        if item_id == 1:
            cd = cd + 1
            print('CD!')
        elif item_id == 2: dvd = dvd + 1
        elif item_id == 3: video = video + 1
        elif item_id == 4: book = book + 1
    count = count + 1

print('CDs in stock:', cd)
print('DVDs in stock:', dvd)
print('Videos in stock:', video)
print('Books in stock:', book)