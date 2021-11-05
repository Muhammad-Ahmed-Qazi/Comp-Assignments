yodafone = 0
ntwo = 0
kofee = 0
satsuma = 0

for count in range(0, 50000):
    code = input('Enter the mobile phone number: (8-digit) ')
    if code[0:3] == '444': yodafone += 1
    elif code[0:3] == '555': ntwo += 1
    elif code[0:3] == '666': kofee += 1
    elif code[0:3] == '777': satsuma += 1

print('Yodafone calls:', yodafone)
print('N2 Network calls:', ntwo)
print('Kofee mobile calls:', kofee)
print('Satsuma mobile calls:', satsuma)