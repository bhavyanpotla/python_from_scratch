a=input('enter the string:')
lower_count = 0
upper_count = 0
other_count = 0

for i in a:
    if i.islower():
        lower_count+=1
    elif i.isupper():
        upper_count+=1
    else:
        other_count+=1


print(f'upper case letters count = {upper_count}')
print(f'lower case letters count={lower_count}')
print(f'other case letters count={other_count}')
