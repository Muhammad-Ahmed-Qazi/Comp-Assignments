correct = 0

for count in range(0, 50):
    number = float(input('Enter any number: '))
    if number >= float(1000) and number <= float(9999): correct += 1

out = 5 - correct
print('This many numbers were out of range:', out, correct)
print('Percentage of numbers out of range:', (out/50) * 100)