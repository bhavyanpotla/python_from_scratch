#Write a program that takes the radius of a circle as input and computes its area
'''
   import math

radius = float(input('enter the radius of the circle:'))
if radius >= 0:
    area = 3.14*radius*radius
    print(f'area of the circle is {area}')
else:
    print('radius cannot be negative enter the radius again!')
'''

#Write a program that takes two integers a and b as input and prints their sum, difference,
#product, quotient, and remainder.
'''
a = int(input('enter a:'))
b = int (input('enter b:'))

sum = a+b
diff = a-b
product = a*b
quotient = a/b
remainder = a%b
print(f'sum is {sum}')
print(f'difference is {diff}')
print(f'product is {product}')
print(f'quotient is {quotient}')
print(f'remainder is {remainder}')
'''
#Write a simple calculator program. It should be able to add, subtract, multiply, and divide
#any two numbers input by the user.
#Note: The user will also specify the operation to perform
'''
print('-------calculator-------')
print('choice 1:add')
print('choice 2:subtract')
print('choice 3:multiply')
print('choice 4:divide')
choice = int(input("enter ur choice among the options mentioned above:"))
a = float(input('enter a:'))
b = float(input('enter b:'))

if choice == 1:
    print(f'sum is {a+b}')
elif choice == 2:
    print(f'difference is {a-b}')
elif choice == 3:
    print(f'product is {a*b}')
elif choice == 4:
    print(f'quotient is {a/b}')
else:
    print('inavlid choice make a choice according to the options!!!')
'''

#Write a program that takes the length and breadth of a rectangle as input and prints its area
#and perimeter.
#Note: If the inputs are invalid, display an appropriate message.
'''
l = float(input('enter the length of the rectangle:'))
b = float(input('enter the breadth of the rectangle:'))
area = l*b
peri = 2*(l+b)

print(f'area is {area}sq.units and perimeter is {peri}units')
'''
# Write a program that takes an integer as input, and displays whether this integer is negative,
#positive, or zero.

'''
integer = int(input('enter an integer to check its nature:'))
if integer > 0:
    print(f'{integer} is positive')
elif integer < 0:
    print(f'{integer} is negative')
else:
    print(f'{integer} is zero')
'''
# Write a program that takes two integers a and b as input and displays whether a < b, a = b,
#or a > b.

'''
a = int(input('enter a:'))
b = int(input('enter b:'))
if a > b:
    print('a>b')
elif a < b:
    print('a<b')
else:
    print('a=b')
    
'''

#Write a program that takes three integers as input and prints their maximum value.

'''
a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))

maximum = max(a,b,c)
print(f'maximum of the 3 inputs given is {maximum}')
'''

#Write a program that takes a three-digit integer as input and prints the sum of its digits.
'''
num = int(input('enter a 3-digit number:'))  
sum = 0
while num>0:
    rem = num % 10
    sum += int(rem)
    num = num / 10
print(f'sum of the digits is {sum}')

'''

#Write a program that takes the marks for 5 subjects as input and calculates the total and
#average marks

'''
marks = []
for i in range(1,6):
    mark = float(input(f'enter the marks of subject-{i}:'))
    marks.append(mark)
total = sum(marks)
average = total / 5

print(f'total marks is {total} and average is {average}')
'''
#Write a program that takes three integers as input and prints the minimum (of the three
#values).

'''
numbers = []
for i in range(1,4):
    number = int(input(f'enter number{i}:'))
    numbers.append(number)
print(f'minimum among these is {min(numbers)}')
'''
#Write a program that takes an integer as input and displays if it is odd or even.

'''
n = int(input('n:'))
if n == 0:
    print(0)
elif n % 2 == 0:
    print(f'{n} is even')
elif n % 2 != 0:
    print(f'{n} is odd')
'''
#Write a program that takes a floating-point value as input and prints its absolute value.
'''
a = float(input())
print(a)
b = round(a)
print(b)
'''
#Write a program that takes an integer as input and checks if it is divisible by 17.
'''
n = int(input('enter a number:'))
if n % 17 == 0:
    print(f'{n} is divisible by 17')
else:
    print(f'{n} is not divisible by 17')
'''
#Write a program that takes a valid letter grade (S/A/B/C/D/E) as input and prints its
#respective grade point (10/9/8/7/6/4).
#Note: If an invalid letter grade is entered, the program should display an appropriate message.
'''
grade = input('enter the grade:').upper()
if grade == 'A' or grade == 'B' or grade == 'C' or grade == 'D' or grade == 'E' or grade == 'S':
    if grade == 'S':
        print('S=10 gpa')
    elif grade == 'A':
        print('A=9 gpa')
    elif grade == 'B':
        print('B=8 gpa')
    elif grade == 'C':
        print('C=7 gpa')
    elif grade == 'D':
        print('D=6 gpa')
    elif grade == 'E':
        print('E=4 gpa')
else:
    print('invalid! , enter the appropriate grade ')  
'''
#Write a program to select one option from the list and display output accordingly.
#Example:
#Please enter your choice:
#1. Check Balance
#2. View Offers
#3. Special Recharge
#Enter 0 to exit

'''
balance = 500
while True:
    print('1. Check Balance')
    print('2. View Offers')
    print('3. Special Recharge')
    print('enter 0 to exit')
    choice = int(input('Please enter your choice:'))
    if choice == 1:
        print('-------------------------------')
        print(f'your balance is {balance}rs')
        print('-------------------------------')
    elif choice == 2:
        print('-------------------------------')
        print('30% Off - introductory offer!')
        print('-------------------------------')
    elif choice == 3:
        print('-------------------------------')
        print('special recharge is worth 299rs')
        print('-------------------------------')
        f = int(input('yes(press 1)/no(press 2)'))
        if f == 1:
            if balance > 299:
                print('-------------------------------')
                print('special recharge successful!')
                print('-------------------------------')
                balance -= 299
                print('-------------------------------')
                print(f'your balance deducted to {balance}rs')
                print('-------------------------------')
            else:
                print('**************************')
                print('insufficient balance for special pack.')
                print('**************************')
    elif choice == 0:
        print('**************************')
        print('thank u pls visit again!')
        print('**************************')
        break
    else:
        print('**************************')
        print('invalid choice , try again!')
        print('**************************')

'''
#Write a program that takes as input the coefficients of the quadratic equation ax2 + bx + c = 0 and
#  prints whether the roots are real or complex.

'''
a = int(input())
b = int(input())
c = int(input())

dis = ((b**2) - (4*a*c))

if dis > 0 :
    print('2 distinct real roots')
elif dis == 0:
    print('2 equal, real roots')
else:
    print("no real roots")
'''
#Input:
#abcde
#abdfe
#Distance: 0-0-1-2-0
#Output: 3
#Input:
#pqxzy
#qpyax
#Distance: 1-1-1-25-1
#Output: 29
'''
str1 = input('enter (string 1) of 5 charcters:')
str2 = input('enter (string 2) of 5 charcters:')
sum = 0
if len(str1) == 5 and len(str2) == 5:
    for i in range(5):
        f = abs(ord(str1[i])-ord(str2[i]))
        sum += f
    print(sum)
else:
    print('enter the strings according to the instruction given!')
'''
#Write a program that takes a 2-letter word as input and prints it in capital letters.
'''
inp = input('enter a (2) letter word:')
if len(inp) == 2 and inp.isalpha():
    inpt = inp.upper()
    print(inpt)
else:
    print('enter a (2) letter word')
'''

#Write a program that takes a character as input and prints the alpha-numeric character (0–9,
#A–Z, a–z are alpha-numeric characters) that is closest to this character.
#Note: If the input character is equidistant from two alpha-numeric values,either one can be printed.

'''
a = input('enter a character:')
print(5<<1)
print(2>>3)
print(2//8)
'''
radius = float(input('enter the radius of the circle:'))
if radius >= 0:
    area = 3.14*radius*radius
    print(f'area of the circle is {area}')
else:
    print('radius cannot be negative enter the radius again!')

a=893456789
b=1004567890
c=a*b
print(f'product of {a} and {b} is {c}')
ph_no = 7386179776
s='jio'
print(f'vishnu phone number is {ph_no} and sim is {s}')

 
