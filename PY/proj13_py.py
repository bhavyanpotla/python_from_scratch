# PASSWORD GENERATOR
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
           'v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
           'Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','_','+','?','/','<','>','/']
n_letters = int(input('enter the no of letters you want in ur password? :'))
n_numbers = int(input('enter the no of  numbers you want in ur password? :'))
n_symbols = int(input('enter the no of symbols you want in ur password? :'))

#type -- 1
password = ''
for i in range(1,n_letters+1):
    char = random.choice(letters)
    password += char
for i in range(1,n_numbers+1):
    char1 = random.choice(numbers)
    password += char1
for i in range(1,n_symbols+1):
    char2 = random.choice(symbols)
    password += char2
print(f'medium={password}')

password_list = []
for i in range(1,n_letters+1):
    char = random.choice(letters)
    password_list += char
for i in range(1,n_numbers+1):
    char1 = random.choice(numbers)
    password_list += char1
for i in range(1,n_symbols+1):
    char2 = random.choice(symbols)
    password_list += char2
random.shuffle(password_list)
password2 = ''
for chr in password_list:
    password2 +=chr
print(f'strong={password2}')

