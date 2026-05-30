# program to find the maximum number from a list of numbers

n = input('enter the elements of the list by spacing:')
num = n.split( )
for i in range(len(num)):
    num[i]=int(num[i]) 
print(num)
max=num[0]
for i in num:
    if(i>max):
        max=i
print(f'The largest number among the ones u eneterd is {max}')
