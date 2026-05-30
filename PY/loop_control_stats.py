#              break             |         continue            |                             pass
count = 10
while count>=0:
    print(count)
    count -= 1
    if count == 7:
        break
    print("hi")
print("out of the loop")

# here while loop is broken at the count = 7 until then 10 9 8 is printed along with the hi.

lis1=['hi','hello','welcome']
n=['krishna','ram','madhav']
for i in lis1:
    for name in n:
        print(i,name)
        if i == 'hello' and name == 'ram':
            break
        print('out from inner loop')

print("out from outer loop!")


count = 1
while count<=10:
    print(count)
    count += 1
    if count == 7:
        continue
    print('hi')
print('out from the loop!')

c = 1
for i in range(11):
    print(c)
    c += 1
    if c == 8:
        continue
    print('hlo')
print('out from the loop!')


for i in range(1,11):
    pass                # pass here is used since the indentation error will occur if we leave loop.
# hence for future use i will use that so i deliberately used pass.
