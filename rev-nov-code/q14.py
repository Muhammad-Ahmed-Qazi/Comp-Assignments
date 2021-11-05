above = 0
below = 0
enquiries = int(input('Enter the number of customer enquiries: '))

for count in range(0, enquiries):
    price = float(input('Enter the house price the customer enquired about: ($) '))
    if price < 100000: below = below + 1
    elif price > 500000: above = above + 1

print('Customers enquiring about houses costing less than $100,000:', below)
print('Percentage of customers enquiring about houses costing more than $500,000: (%)', (above / enquiries) * 100)
