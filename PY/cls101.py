'''
def pri(n):
    for i in range(n+1):
        print(i)
    
n = int(input('enter the value of n:'))
pri(n)
'''
'''
def k(n):
    if n == 0:
        return 1
    print(n)
    k(n-1)
k(20)
'''
'''
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*fact(n-1)
    
n = 5
print(fact(n))
'''
'''
def sumof(n):
    if n==0:
        return 0
    else:
        return n+sumof(n-1)
print(sumof(100))
'''
'''
def func(a,b):
    if b == 0:
        return 1
    else:
        return a*func(a,b-1)
print(func(2,10))
'''
'''
def reverse(a):
    if len(a)<=1:
        return a
    else:
        return a[-1]+reverse(a[:-1])
print(reverse('vishnu'))
'''

    