import random
a=random.randint(1,100)         #1<=a<=100
print(a)
b=random.randrange(1,100)       #1<=a<100
print(b)
c=random.random()               #this will return a floating point number b/w 0.0 and 1.0 but 1.0 excluded
print(c)
d=random.uniform(1,100)
print(d)
l=[-1,-98,46,83]
print(random.choice(l))   #83(in my output)
print(l)                  #[-1, -98, 46, 83]
random.shuffle(l)
print(l)
 

