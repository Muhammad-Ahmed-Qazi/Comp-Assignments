x = 1
while x != 0:
    x = float(input('Enter a value for x: (Enter 0 to end the program) '))
    if x < 1 and x > 0:
        n = (x * x) / (1 - x)
        print(n, x)
