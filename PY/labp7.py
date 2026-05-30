d = int(input('enter a number:'))
t = d
b = ""
if t == 0:
    b = "0"
while t > 0:
    r = t % 2
    b = str(r) + b
    t //= 2

print(f"Decimal {d} in Binary is: {b}")