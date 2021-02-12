people = int(input('Enter the number of tickets you want to buy: '))
discount = float(0)
cost = float(0)

if people >= 3:
    discount = 0.1

cost = (people * 5) * (1 - discount)
print('This is the cost of the tickets:', cost)