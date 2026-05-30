#strong number or not
n = int(input('enter a number:'))
temp = n
total_sum = 0
while temp>0:
    digit = temp%10
    factorial = 1
    for i in range(1,digit+1):
        factorial*=i
    
    total_sum+=factorial
    temp//=10

if(total_sum == n):
    print(f"{n} is a Strong Number!")
else:
    print(f"{n} is not a Strong Number!")


