binary = int(input('enter a number:'))
temp = binary
decimal = 0
power = 0

while temp > 0:
    digit = temp % 10
    decimal += (digit * (2 ** power))
    power += 1
    temp //= 10

print(f"Decimal equivalent of {binary} is: {decimal}") 
