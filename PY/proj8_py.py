#rock paper scissors game in python


import random

print('Rules of the game:')
print('(i) Rock wins against Scissors')
print('(ii) Scissors wins against Paper')
print('(iii) Paper wins against Rock')

print('0. Rock')
print('1. Paper')
print('2. Scissors')

user = int(input('Enter your choice (0/1/2): '))
computer = random.randint(0, 2)

choices = ['Rock', 'Paper', 'Scissors']

print(f'You chose: {choices[user]}')
print(f'Computer chose: {choices[computer]}')

if user == computer:
    print('Draw 🤝')
elif (user == 0 and computer == 2) or \
     (user == 2 and computer == 1) or \
     (user == 1 and computer == 0):
    print('You WON 🎉')
else:
    print('You LOST ❌')
