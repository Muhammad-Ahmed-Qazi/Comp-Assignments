count = 0
correct = 0

while count < 5:
    code = input('Enter the five-digit barcode: (E.g. 01234) ')
    if len(code) > 5: continue
    check = ((int(code[0]) * 3) + (int(code[1]) * 3) + (int(code[2]) * 3) + (int(code[3]) * 3)) % 10
    print(check)
    if check == int(code[4]): correct += 1
    count += 1

print('This many barcodes were correct:', correct)