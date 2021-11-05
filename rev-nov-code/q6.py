stat = 1
curr_balance = 600
daily_limit = 200
request = int(input('Enter the sum of money you want to withdraw: ($) '))

while stat == 1:
    if request > curr_balance: print('Withdrawal refused because amount entered is greater than your current balance!'); break
    if request > daily_limit: print('Withdrawal refused because amount entered is greater than your daily limit!'); break

    if curr_balance < 100: charges = 0.02 * curr_balance; print('Charges: $' + str(charges))
    elif curr_balance >= 100: print('No charges made!')