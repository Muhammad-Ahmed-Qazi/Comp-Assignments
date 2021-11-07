d1 = 0
d2 = 0
d3 = 0
d4 = 0
palindrome = 0

for count in range(0, 50):
    number = input('Enter any positive 4-digit number: ')
    d1 = number[0]
    d2 = number[1]
    d3 = number[2]
    d4 = number[3]
    if d1 == d4 and d2 == d3: palindrome += 1; print('Palindrome!')

print('Percentage of numbers that were palindromes:', (palindrome/50) * 100)