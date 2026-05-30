n = int(input('enter:'))
sum_div = 0
for i in range(1,n):
    if n%i == 0:
        sum_div+=i
if n == sum_div:
    print(f'{n} is a perfect number')
else:
    print(f'{n} is not a perfect number')