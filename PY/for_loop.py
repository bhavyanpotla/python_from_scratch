#                                     FOR LOOP
# for variable_name sequence:
#  statement(s)

names=['jenny','ram','rahul','payal']
for name in names:
    print(name)
for num in [12,93,84,-20,91,73,0,-24]:
    print(num)
name = 'bhavyan'
users = ['ram','krishna','govind','narasimha','maruthi']

for i in users:
    print(i)

    if i == 'ram':
        print('hello ram!')
    if i == 'krishna':
        print('hello krishna!')
    if i == 'govind':
        print('hello govind!')
    if i == 'narasimha':
        print('hello narasimha!')
    if i == 'maruthi':
        print('hello hanuman!')


li=[2,3,5,-2,10]
sq_li=[]
for i in li:
    square = i**2
    sq_li.append(square)
    print(f'the square of {i} is {sq_li}')

print(sq_li)
