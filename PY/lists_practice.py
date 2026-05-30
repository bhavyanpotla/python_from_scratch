list1=[1,2,3,4,5]
list2=['samantha','poojahegde','norafatehi']
list3=[list1,list2]
print(list3[1][2])   #norafatehi
print(list3[1][0])  #samantha
print(list3[0][4])  #5

list4=list1+list2
print(list4)             #[1, 2, 3, 4, 5, 'samantha', 'poojahegde', 'norafatehi']

#inbulit functions usage in lists

l=[123,345,456,567,678]
l.append(789)
n=l.count(123)
print(n)
l.insert(6,890)
print(l)
l.remove(890)
print(l)
print(l.pop(5))
print(l)
print(l.pop())  #678
print(l[0])
print(l[1])
del l[0:1]
print(l)
l.extend([123])
print(l)
l[0:1]=[123,345]
print(l)
l.extend([678])
l[4:5]=[678,123]
print(l)
l.remove(678)
print(l)
l.remove(123)
print(l)
l.sort()
print(l)
print(min(l))
print(max(l))
print(sum(l))
print(min(list2))
print(max(list2))

print(l)                #[123, 345, 456, 567, 678]
print(l[1:3])           #[345,456]
print(l[1:2])

x=[1,2,3,4,5,6]   #using the slicing technique to skip two elements and print the rest!
result=x[::2]
print(result)    #[1,3,5]
er = x[1:]
print(er)         #[2, 3, 4, 5, 6]