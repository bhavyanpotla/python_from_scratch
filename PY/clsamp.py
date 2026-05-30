'''
x = [1,2,4,6,8]
for i in x:
    if i%2 == 0:
        x.remove(i)
    print(x)
'''
'''
p = lambda x:x[1]*10
print(p([1,2,3,4,5]))
print(type(p))
'''
'''
p = lambda x:'even' if x%2 == 0 else 'odd'
print(p(4))
'''
 
'''
def addneven_list(l):
    total = 0
    for i in l:
        if i%2==0:
            total+=i
    return total
print(addneven_list([1,2,3,4,5,6,7,8,9,10]))
'''
'''
def addnodd_list(l):
    total = 0
    for i in l:
        if i%2!=0:
            total+=i
    return total
print(addnodd_list([1,2,3,4,5,6,7,8,9,10]))
'''

'''
def producteven(l):
    pro = 1
    for i in l:
        if i%2==0:
            pro *= i
    return pro
print(producteven([1,2,3,4,5,6,7,8,9,10]))
 
'''
'''
def productodd(l):
    pro = 1
    for i in l:
        if i%2!=0:
            pro *= i
    return pro
print(productodd([1,2,3,4,5,6,7,8,9,10]))
'''

'''

def addn5_list(l):
    total = 0
    for i in l:
        if i%5==0:
            total+=i
    return total
print(addn5_list([1,2,3,4,5,6,7,8,9,10]))
'''

'''
def addn_list(l, r):
    total = 0
    for i in l:
        if r == "even" and i % 2 == 0:
            total += i
        elif r == "odd" and i % 2 != 0:
            total += i
        elif r == "div5" and i % 5 == 0:
            total += i
    return total

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(addn_list(li, "even"))  
print(addn_list(li, "odd"))   
print(addn_list(li, "div5"))  
'''
#take a list 1 to 10 and perform these operations:
#1.fiter all the odds
#2.square the resultant
#3.sum of all elements

'''
first = list(filter(lambda x:x%2==0,l))
print(first)
second = list(map(lambda x:x**2,first))
print(second)
from functools import reduce
third = reduce(lambda x,y:x+y,second)
print(third)
'''
from functools import reduce

l = [1,2,3,4,5,6,7,8,9,10]
print((f := list(filter(lambda x: x%2==0, l))), (s := list(map(lambda x: x**2, f))), reduce(lambda x, y: x+y, s))


