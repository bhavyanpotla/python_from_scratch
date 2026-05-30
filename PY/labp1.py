n = int(input('enter a number:'))
is_prime = True
if n>1:
    for i in range(2,n):
        if (n%i) == 0:
            is_prime = False
            break
    if is_prime == True:
        print(f"{n} is a prime")
    else:
        print(f"{n} is not a prime number.")
else:
    print("primes cant be under 1")
