high = 0.00
low = 2000.00
total = 0.00

for count in range(0, 1000):
    weight = float(input('Enter the weight of the item: '))
    if weight < low:
        low = weight
    if weight > high:
        high = weight
    total = total + weight

avg = total / 1000
print('This is the mean weight of all the items:', avg)
print('This is the highest weight of all the items:', high)
print('This is the lowest weight of all the items:', low)
