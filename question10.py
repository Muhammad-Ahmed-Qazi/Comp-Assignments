players = int(input('Enter the number of players: '))
hours = float(input('Enter the number of hours the players will play: '))

charge = 0
discount = 0.00

club = input('Enter "y" if you are a member of the club and if you are not, then enter "n": ')
if club == 'y':
    pin_m = int(input('Enter the 4-digit PIN code given by the club: (member) '))
    pin_s = int(input('Enter the 4-digit PIN code given by the club: (staff) '))
    if pin_m == pin_s:
        charge = 4
    else:
        charge = 5
else:
    print('You are not a member of the club!')

cost = players * (hours * charge)
if players >= 3 and hours >= 3:
    discount = cost * 0.35
elif players >= 3:
    discount = cost * 0.25

cost = cost - discount
print('This is the hire charge:', cost)