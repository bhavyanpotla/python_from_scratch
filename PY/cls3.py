#reverse a string without slicing
reversed_str = ""
q = input('enter a string:')
for i in q:
    reversed_str = i+reversed_str
print(reversed_str)

    