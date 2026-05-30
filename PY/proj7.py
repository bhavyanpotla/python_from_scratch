#coin master inspiration :: digging and inserting the wealth(using the nested lists)
l1=[1,1,1]
l2=[1,1,1]
l3=[1,1,1]
l=[l1,l2,l3]
print(l)
print('\n',l1,'\n',l2,'\n',l3)
c=input('enter a position to hide the coins(row column):')
a=int(c[0])
b=int(c[1]) 
l[a-1][b-1]='x'
print('\n',l1,'\n',l2,'\n',l3)
