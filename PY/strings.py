# Creating and displaying strings
print('bhavyan')                          # bhavyan

# error:: NameError – bhavyan is treated as a variable, not a string
# print(bhavyan)

print('bhavyan')                          # bhavyan


# Quotes in strings
# error:: SyntaxError – single quote inside single-quoted string
# print('bhavyan's laptop')

print("bhavyan's laptop")                 # bhavyan's laptop

# error:: SyntaxError – printf is not a Python function and \s is invalid
# printf('bhavyan'\s "laptop")

print('bhavyan\'s "laptop"')              # bhavyan's "laptop"


# String repetition
print('bhavyan' * 10)
# bhavyanbhavyanbhavyanbhavyanbhavyanbhavyanbhavyanbhavyanbhavyanbhavyan

print('bhavyan ' * 10)
# bhavyan bhavyan bhavyan bhavyan bhavyan bhavyan bhavyan bhavyan bhavyan bhavyan 

# error:: NameError – bhavyan is not defined as a variable
# print(bhavyan * 10)


# Escape characters in strings
# error:: unicodeescape error – \u is treated as unicode escape
# print('c:\users\bhavy')

print('c:\\users\\bhavy')                 # c:\users\bhavy


# String variables
name = 'bhavyan'
print(name)                               # bhavyan

# error:: NameError – laptop variable not defined
# print(name + laptop)

print(name + 'laptop')                    # bhavyanlaptop

name = name + 'laptop'
print(name)                               # bhavyanlaptop

# error:: TypeError – subtraction not supported for strings
# name = name - 'laptop'

print(name)                               # bhavyanlaptop

name = name + ' laptop'
print(name)                               # bhavyanlaptop laptop


# String indexing
text = 'python'
print(text)                               # python

print(text[0])                            # p
print(text[3])                            # h
print(text[-1])                           # n
print(text[-6])                           # p

# String slicing
print(text[3:-1])                         # ho
print(text[2:5])                          # tho
print(text[2:6])                          # thon
print(text[0:1])                          # p
print(text[0:2])                          # py
print(text[1:1000000])                    # ython
print(text[1:])                           # ython
print(text[:4])                           # pyth

# error:: TypeError – strings are immutable (cannot change characters)
# text[0:3] = 'PYT'


# Length of string
print(len(text))                          # 6


# Multiline strings using escape sequence
text1 = 'My name is bhavyan naidu , this is my laptop.'
print(text1)
# My name is bhavyan naidu , this is my laptop.

text1 = 'My name is bhavyan naidu \n this is my laptop.'
print(text1)
# My name is bhavyan naidu
#  this is my laptop.



 