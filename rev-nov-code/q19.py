data = []

for count in range(0, 3):
    number = int(input('Enter any number: '))
    data.append(number)

data.sort()
print([item for item in data])