'''
#extracting the digits from a number and printing
n = int(input('enter a number:'))
p = 1
while n//p>=10:
    p*=10
while p>0:
    print(n//p)
    n%=p
    p//=10

'''
'''
#gcd of 2 numbers
a=int(input('num1:'))
b=int(input('num2:'))
while b!=0:
    a , b = b , a % b
print('gcd is :',a)
'''
 
'''
#finding gcd using math library
import math
a=int(input('num1:'))
b=int(input('num2:'))
gcd = math.gcd(a,b)
print(f'gcd of {a} and {b} is {gcd}')
'''

'''
#finding the no of digits in a number
a =int(input('num='))
count = 0 
while a!=0:
    a//=10
    count+=1
print(count)
'''
'''
#finding if num is a perfect square or not
a=int(input('num:'))
is_square = False
i=1
while i*i <= a:
    if i*i == a:
        is_square = True
        break
    i+=1
print(is_square)
'''
'''
#finding using math lib
import math
a=int(input('num:'))
root = math.sqrt(a)
if root == int(root):
    print(True)
else:
    print(False)
'''
'''
a=int(input('num1:'))
b=int(input('num2:'))
c=int(input('num3:'))
d=int(input('num4:'))
e=int(input('num5:'))

avg = (a+b+c+d+e)/5

max1 = a if a>b else b
max2 = max1 if max1>c else c
max3 = max2 if max2>d else d
maximum = max3 if max3>e else e

min1 = a if a < b else b
min2 = min1 if min1 < c else c
min3 = min2 if min2 < d else d
minimum = min3 if min3 < e else e

print('avg is:',avg)
print('maximum is:',maximum)
print('minimum is:',minimum)
'''
'''
import math

def absolute_value(n):
    return math.sqrt(n**2)

print(absolute_value(-25))  
print(absolute_value(10)) 
'''
'''
#palindrome number
num = int(input('enter a 3 digit number:'))
rev = 0
org = num
while num>0:
    rem = num % 10
    rev = rev*10 + rem
    num = num // 10
if(rev == org):
    print(f'{org} is a palindrome number')
else:
    print(f'{org} is not a palindrome number')
'''
'''
#armstrong number
num = input('enter a number:')
n = len(num)
sum_of_powers = 0
for i in num:
    sum_of_powers+=int(i)**n
if(sum_of_powers == int(num)):
    print(True)
else:
    print(False)
'''
'''
#reversing a number
a = int(input('enter a 4 digit number:'))
rev = 0
org = a
while a>0:
    rem = a%10
    rev = rev*10+rem
    a = a//10
print(org)
print(rev)
'''
'''
#time in seconds, mins,hrs
time = int(input('enter the no of total seconds:'))
hrs = time // 3600
rem_sec = time % 3600
mins = time // 60
sec = rem_sec % 60
print(f"{hrs} Hours,{mins} Minutes, and {sec} Seconds")
'''
'''
#basic calculator
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /, //, %, **): ")
num2 = float(input("Enter the second number: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 == 0:
        result = "Error! Division by zero is undefined."
    else:
        result = num1 / num2
elif operator == '//':
    if num2 == 0:
        result = "Error! Floor division by zero."
    else:
        result = num1 // num2
elif operator == '%':
    if num2 == 0:
        result = "Error! Modulo by zero."
    else:
        result = num1 % num2
elif operator == '**':
    result = num1 ** num2
else:
    result = "Invalid operator entered!"
print(f"Result: {result}")
'''
'''
# 1. Input: Get sides and sort them so 'c' is always the largest
sides = [float(input("Side 1: ")), float(input("Side 2: ")), float(input("Side 3: "))]
sides.sort()
a, b, c = sides[0], sides[1], sides[2]

# 2. Validity Check
if a + b > c:
    print("The triangle is valid.")
    
    # 3. Classify by Sides
    if a == b == c:
        side_type = "Equilateral"
    elif a == b or b == c or a == c:
        side_type = "Isosceles"
    else:
        side_type = "Scalene"
        
    # 4. Classify by Angles (using Pythagoras)
    # Using round() to avoid small floating point errors
    a_sq_plus_b_sq = round(a**2 + b**2, 2)
    c_sq = round(c**2, 2)
    
    if a_sq_plus_b_sq == c_sq:
        angle_type = "Right"
    elif a_sq_plus_b_sq > c_sq:
        angle_type = "Acute"
    else:
        angle_type = "Obtuse"
        
    print(f"Classification: {side_type} and {angle_type} triangle.")

else:
    print("Invalid Triangle: The sum of two sides must be greater than the third.")
'''
'''
# 1. Inputs
color = input("Enter the light color (Red, Yellow, Green): ").strip().capitalize()
action = input("Enter your action (Walk, Drive): ").strip().capitalize()

# 2. Nested Logic
if color == "Red":
    if action == "Walk":
        print("Allowed: Pedestrians may cross safely.")
    elif action == "Drive":
        print("Prohibited: You must stop your vehicle.")
    else:
        print("Invalid action.")

elif color == "Yellow":
    if action == "Walk":
        print("Caution: Do not start crossing; wait for the next cycle.")
    elif action == "Drive":
        print("Caution: Clear the intersection or prepare to stop.")
    else:
        print("Invalid action.")

elif color == "Green":
    if action == "Walk":
        print("Prohibited: Pedestrians must wait; vehicles are moving.")
    elif action == "Drive":
        print("Allowed: You may proceed through the intersection.")
    else:
        print("Invalid action.")

else:
    print("Invalid color entered. Please use Red, Yellow, or Green.")
'''
##-----------------------------ATM-------------------
'''
pin = '2580'
balance = 5000.0
attempts = 3
login = False

# 1. PIN Verification Loop
while attempts > 0:
    entered_pin = input('Enter the PIN: ').strip()

    if pin == entered_pin:
        print('--- Login Successful! ---')
        login = True
        break
    else:
        attempts -= 1
        print(f'Incorrect PIN. {attempts} attempts left!')

# 2. Continuous Menu Loop (Only runs if login is True)
while login:
    print("\n" + "="*20)
    print("      ATM MENU")
    print("="*20)
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        print(f'\nYour account balance is: ₹{balance}')
        
    elif choice == '2':
        # Using float to handle decimals correctly
        withdraw = float(input('Enter the amount to withdraw: '))
        if withdraw > balance:
            print('❌ Insufficient funds!')
        elif withdraw <= 0:
            print('❌ Invalid amount!')
        else:
            balance -= withdraw
            print(f'✅ ₹{withdraw} withdrawn successfully.')
            print(f'New balance: ₹{balance}')
            
    elif choice == '3':
        deposit = float(input('Enter the amount to deposit: '))
        if deposit <= 0:
            print('❌ Invalid amount!')
        else:
            balance += deposit
            print(f'✅ ₹{deposit} deposited successfully.')
            print(f'New balance: ₹{balance}')
            
    elif choice == '4':
        print("\nThank you for using our ATM. Goodbye!")
        login = False # This breaks the loop and "logs out" the user
        
    else:
        print('⚠️ Invalid selection! Please try again.')

# This only prints if the user failed the 3 attempts at the start
if not login and attempts == 0:
    print('\nAccount blocked. Please contact your bank!')
'''
'''
#check prime or not using the while loop
n = int(input('enter a number:'))
if n<2:
    print("not prime")
else:
    a = 2
    is_prime = True

    while a<n:
        if n%a == 0:
            is_prime = False
            break
        a += 1
    if is_prime:
        print(f'{n} is a prime number')
    else:
        print(f"{n} isn't a prime number")
'''
'''
#to find the factorial of number using while loop

n = int(input('enter a number:'))
org = n
res = 1
while n>0:
    res = res * n
    n -= 1
print(f'factorial of {org} is {res}')
'''
'''
#Write a program that reads numbers from the user until a negative number is entered. Print the sum,
#count, and average of positive numbers.

tot = 0
count = 0 
avg = 0
n = 0
while n>=0:
    n = int(input('enter a number:'))
    count+=1
    tot+=n
    avg = tot/count
print(f'count = {count};sum = {tot};average = {avg}')
'''

'''
#Write a program that simulates a number guessing game: the program picks a number between 1 and
#100, and the user keeps guessing until they get it right. Print 'Too High' or 'Too Low' as hints.

import random

correct_guess = random.randint(1, 100)
attempts = 5   

print(f"You have {attempts} attempts to guess the number!")

while attempts > 0:
    guess = int(input('Enter your guess: '))

    if guess > correct_guess:
        print('Too high!')
    elif guess < correct_guess:
        print('Too low!')
    else:
        print(f"You're right! The correct number was {correct_guess}")
        break   

    attempts -= 1  
    
    if attempts > 0 and guess != correct_guess:
        print(f"Remaining attempts: {attempts}")
    elif attempts == 0:
        print(f"Game Over! You ran out of chances. The number was {correct_guess}.")
'''
'''
#Q1. Write a program to print the Fibonacci series up to N terms using a while loop. 
# Also check if a user-given  number is a Fibonacci number. 
import math
n = int(input('how many:'))
a,b = 0,1
count = 1
print(f'fibanocci sequence upto {n} terms:')
while count<n:
    print(a,end='')
    nth = a+b
    a = b
    b = nth
    count += 1
    print()
def is_perfsq(x):
    s = int(math.sqrt(x))
    return s*s == x
user_num = int(input("Enter a number to check if it's a Fibonacci number: "))
c1 = 5*(user_num**2)+4
c2 = 5*(user_num**2)-4

if is_perfsq(c1) or is_perfsq(c2):
    print(f'yes! , {user_num} is a fibanocci number')
else:
    print(f'No! , {user_num} is not a fibanocci number')
'''

'''
balance = 1000.0  # Starting balance
is_running = True

print("--- Welcome to the Simple ATM ---")

while is_running:
    print("\nMain Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    choice = input("Select an option (1-4): ")

    if choice == '1':
        print(f"Your current balance is: ${balance:,.2f}")

    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"Successfully deposited ${amount:,.2f}")
        else:
            print("Invalid amount. Please deposit a positive value.")

    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds! Transaction cancelled.")
        elif amount <= 0:
            print("Invalid amount. Please enter a positive value.")
        else:
            balance -= amount
            print(f"Successfully withdrew ${amount:,.2f}")

    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        is_running = False  # This breaks the loop
        
    else:
        print("Invalid selection. Please try again.")
'''
'''
#gcd and lcm of 2 numbers using a while loop
n1 = int(input('enter num1:'))
n2 = int(input('enter num2:'))
a = n1
b = n2
while b!=0:
    rem = a%b
    a = b
    b = rem
gcd = a
lcm = (n1*n2)//gcd
print('gcd is',gcd)
print('lcm is',lcm)
'''
'''
#prime factors of a number
num = int(input('enter a number to write its prime factors:'))
div = 2
print(f'the prime factors of the {num} are:')
while num>1:
    if num%div == 0:
        print(div)
        num = num // div
    else:
        div+=1
print('done')
'''
'''
n = int(input("Enter the number of rows (N): "))

# Row counter
row = 1

while row <= n:
    # Column counter starts at 1 for every new row
    col = 1
    
    # Inner loop prints numbers from 1 up to the current row number
    while col <= row:
        print(col, end=" ")
        col += 1
    
    # Move to the next line after finishing a row
    print()
    
    row += 1
'''
'''
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = []

for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)

print(f"Flattened list: {flat_list}")
'''
'''
#hollow rectangle of stars
r = int(input('enter the no of rows:'))
c = int(input('enter the no of columns:'))
for i in range(1,r+1):
    for j in range(1,c+1):
        if i == 1 or i == r or j == 1 or j == c:
            print('*',end = '')
            continue
        print(' ',end = '')
    print()

'''
'''
stored_pin = "1234"
attempts_allowed = 3

for i in range(1, attempts_allowed + 1):
    user_input = input(f"Attempt {i}: Enter your 4-digit PIN: ")

    if user_input == stored_pin:
        print("Login Successful! Welcome to your account.")
        break  # Exit the loop immediately on success
    
    # If the PIN is wrong
    else:
        remaining = attempts_allowed - i
        if remaining > 0:
            print(f"Incorrect PIN. You have {remaining} attempts left.")
            continue  # Skip the rest of this iteration and prompt again
    
else:
    # This block runs only if the loop finishes without a 'break'
    print("\n" + "!" * 30)
    print("ACCOUNT LOCKED. Too many failed attempts.")
    print("Please contact customer support to reset your PIN.")
'''
'''
#parsing string
data = input("Enter a string (mix of letters, spaces, and numbers): ")
collected_letters = ""

print("\nParsing string...")

for char in data:
    # 1. Stop at any digit
    if char.isdigit():
        print(f"Digit '{char}' found. Stopping parser.")
        break 
    
    # 2. Skip spaces
    if char.isspace():
        continue # Ignore space and move to the next character
        
    # 3. Collect only alphabets
    if char.isalpha():
        collected_letters += char
    else:
        # This handles symbols like @, #, !, etc.
        continue

print(f"Final collected string: {collected_letters}")
'''
'''
sentence = "Hello World"
words = sentence.split()
reversed_words = []

for word in words:
    reversed_words.append(word[::-1])

# Join the list back into a single string with spaces
result = " ".join(reversed_words)
print(f"Original: {sentence}")
print(f"Result:   {result}")
'''
'''
def most_freq(a):
    if not a:
        return None
    max_count = 0
    freq = a[0]

    for i in range(len(a)):
        current_char = a[i]
        current_count = 0

        for j in range(len(a)):
            if a[j] == current_char:
                current_count+=1
            
        if current_count>max_count:
            max_count = current_count
            freq = current_char
    return freq
inp = input('enter a string:')
print(f'most frequent character in the string {inp} : "{most_freq(inp)}"')
'''

'''
def most_frequent(text):
    if not text:
        return None
    max_c = 0 
    freq = text[0]

    for i in range(len(text)):
        current_char = text[i]
        current_count = 0

        for j in range(len(text)):
            if text[j] == current_char:
                current_count+=1
        
        if current_count>max_c:
            max_c = current_count
            freq = current_char
    return freq
string = input('enter a string:')
print(f'maximum occured character in the {string} is : "{most_frequent(string)}"')
'''
'''
def compress(s):
    if not s:
        return ""

    res = ""       # This will hold our final answer (a3b3...)
    count = 1      # We start counting the first letter
    prev = s[0]    # This is the letter we are currently counting

    # Loop through the string starting from the second character
    for i in range(1, len(s)):
        curr = s[i] # The "current" letter we are looking at
        
        if curr == prev:
            # If it's the same letter, just increase the count
            count = count + 1
        else:
            # If it's a NEW letter, save the OLD letter's info
            res = res + prev         # Add the letter
            res = res + str(count)   # Add the count
            
            # Now, reset for the new letter
            prev = curr
            count = 1
            
    # The loop finishes, but the very last group is still "in the air"
    # We have to save it one last time
    res = res + prev
    res = res + str(count)

    return res

print(compress("aaabbbcc")) # Result: a3b3c2
'''
'''
def find_palindromes(text):
    for i in range(len(text)):
        for j in range(i+1,(len(text)+1)):
            sub_string = text[i:j]

            if sub_string == sub_string[::-1] and len(sub_string) > 1:
                print(sub_string)

a = input('enter a string:').replace(" ","").lower()
print(find_palindromes(a))
'''
'''
def check_password(p):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False 

    for i in range(len(p)):
        char = p[i]

        if 'A'<=char<='Z':
            has_upper = True
        elif 'a'<=char<='z':
            has_lower = True
        elif '0'<=char<='9':
            has_digit = True
        else:
            has_special = True
    is_valid = True

    if len(p)<8:
        print("Missing: Minimum 8 characters")
        is_valid = False
    if not has_upper:
        print("Missing: At least one uppercase letter")
        is_valid = False
    if not has_lower:
        print("Missing: At least one lowercase letter")
        is_valid = False
    if not has_digit:
        print('Missing: At least one digit')
        is_valid = False
    if not has_special:
        print('Missing: Atleast one special character')
        is_valid = False
    if is_valid:
        print('your password is secure!')

password = input('enter ur password:')
print(check_password(password))
'''

'''
def reaarnge_vowels(text):
    vowels = 'aeiouAEIOU'
    vowels_bucket = ""
    consonants_bucket = ""
    for i in range(len(text)):
        char = text[i]

        is_vowel = False
        for v in range(len(vowels)):
            if char == vowels[v]:
                is_vowel = True
                break

        if is_vowel:
            vowels_bucket+=char
        else:
            if 'a'<=char.lower()<='z':
                consonants_bucket+=char
            else:
                consonants_bucket+=char
    return vowels_bucket+consonants_bucket

input_str = "alphabet"
print("Original:", input_str)
print("Rearranged:", reaarnge_vowels(input_str))

'''

'''
def remove_duplicates(nums):
    unique = []
    for i in range(len(nums)):
        if nums[i] not in unique:
            unique.append(nums[i])
    return unique
print(remove_duplicates([1,2,3,4,1,2,3,4,5,6,7,4,6,12]))
'''
'''
def flatten(matrix):
    flat_list = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            flat_list.append(matrix[i][j])
    return flat_list
print(flatten([[1,2],[3,4],[5,6],[7]]))
'''
'''
numbers = [12, 7, 22, 19, 8, 10, 3, 1]

evens = []
odds = []

# Loop through the list using indexing
for i in range(len(numbers)):
    num = numbers[i]
    
    # Check if the number is even
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

# Print the final results
print("Original List:", numbers)
print("Even Numbers: ", evens)
print("Odd Numbers:  ", odds)
'''
'''
# Matrix A (2x3)
A = [[1, 2, 3],
     [4, 5, 6]]

# Matrix B (3x2)
B = [[7, 8],
     [9, 10],
     [11, 12]]

# 1. Initialize the Result matrix with zeros (size 2x2)
# Row count of A by Column count of B
result = [[0, 0],
          [0, 0]]

# 2. Outer loop: Iterate through rows of A
for i in range(len(A)):
    
    # 3. Middle loop: Iterate through columns of B
    for j in range(len(B[0])):
        
        # 4. Inner loop: Iterate through rows of B (or columns of A)
        # This performs the "Dot Product"
        for k in range(len(B)):
            result[i][j] = result[i][j] + (A[i][k] * B[k][j])

# 5. Print the final matrix
print("Result of A x B:")
for row in result:
    print(row)
'''

'''
#unpacking a tuple
person = ("Alice", 25, "Mumbai")

# Unpacking
name, age, city = person

print("Name:", name)
print("Age:", age)
print("City:", city)
'''
'''
# A tuple containing student records (Name, Marks)
students = (
    ("Alice", 88),
    ("Bob", 95),
    ("Charlie", 78),
    ("David", 92),
    ("Eve", 85)
)

# 1. Convert the tuple to a list so we can sort it
student_list = list(students)

# 2. Sort the list
# key=lambda x: x[1] tells Python to look at the marks (index 1)
# reverse=True makes it descending (highest marks first)
student_list.sort(key=lambda x: x[1], reverse=True)

# 3. Print the results
print("Rank | Student Name | Marks")
print("-" * 28)
for i in range(len(student_list)):
    name = student_list[i][0]
    marks = student_list[i][1]
    print(f"{i+1:4} | {name:12} | {marks}")
'''

'''
data = (1, 2, 8, 3, 2, 2, 2, 5, 1)

results = []
processed = []

for item in data:
    # Only act if we haven't counted this number yet
    if item not in processed:
        # 1. Use count() to find frequency
        num_count = data.count(item)
        
        # 2. Add the pair (item, num_count) to our list
        results.append((item, num_count))
        
        # 3. Mark as processed so we don't count it again
        processed.append(item)

# Convert list of pairs to a final tuple
final_output = tuple(results)

print(final_output)
# Output: ((1, 2), (2, 4), (8, 1), (3, 1), (5, 1))
'''
'''
# A tuple of coordinate tuples (x, y)
points = ((1, 2), (4, 6), (1, 1), (10, 12), (3, 3))

# Initialize min_distance with a very large number
min_distance = float('inf')
closest_pair = None

# 1. Outer loop to pick the first point
for i in range(len(points)):
    p1 = points[i]
    
    # 2. Inner loop to pick the second point
    for j in range(i + 1, len(points)):
        p2 = points[j]
        
        # 3. Calculate distance: sqrt((x2-x1)^2 + (y2-y1)^2)
        # We use ** 0.5 for the square root
        dist = ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5
        
        # 4. Check if this is the closest we've found so far
        if dist < min_distance:
            min_distance = dist
            closest_pair = (p1, p2)

# Final Result
print(f"The closest points are {closest_pair[0]} and {closest_pair[1]}")
print(f"The distance between them is: {min_distance:.2f}")
'''

'''
data = (1, 2, 3, 4, 5, 6, 7)
k = 3

# 1. Handle cases where k is larger than the tuple length
# Using the modulo operator (%) keeps k within the valid range
n = len(data)
k = k % n

# 2. Slice and Swap
# data[-k:] gets the last k elements
# data[:-k] gets everything from the start up to the last k elements
rotated_tuple = data[-k:] + data[:-k]

# Final Result
print("Original:", data)
print(f"Rotated by {k}:", rotated_tuple)
'''
