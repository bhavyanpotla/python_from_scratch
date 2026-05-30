'''
l = [1,2,3,4,5]
print(list(map(lambda x:x**2,l)))

'''
'''
l=[1,2,3,4,5]
print(l)
print(list(map(lambda x:x>4,l)))
print(list(filter(lambda x:x>4,l)))

'''
from functools import reduce
l = [1,2,3,4,5,6,7,8,9,10]
print((reduce(lambda x,y:x+y,l)))


