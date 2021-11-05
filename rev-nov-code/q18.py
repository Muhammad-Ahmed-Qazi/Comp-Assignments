classical_list = []
rock = 0; soul = 0; pop = 0; jazz = 0; classical = 0

for count in range(0, 1500):
    name = input('Enter your name: ')
    print('1: Rock, 2: Soul, 3: Pop, 4: Jazz, 5: Classical')
    choice = int(input('Enter your preferred music: '))
    if choice == 1: rock += 1
    elif choice == 2: soul += 1
    elif choice == 3: pop += 1
    elif choice == 4: jazz += 1
    elif choice == 5: classical += 1; classical_list.append(name)

print('Students who chose classical music: ')
print([item for item in classical_list])
print('--------------------------List End--------------------------')
print('Rock:', (rock/1500) * 100, 'Soul:', (soul/1500) * 100, 'Pop:', (pop/1500) * 100, 'Jazz:', (jazz/1500) * 100, 'Classical:', (classical/1500) * 100)
