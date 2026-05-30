print("Armstrong numbers between 1 and 100:")
for num in range(1, 101):
    n = len(str(num))  
    temp = num
    total_sum = 0
    
    while temp > 0:
        digit = temp % 10
        total_sum += (digit ** n)  
        temp //= 10
        
    if total_sum == num:
        print(num)

