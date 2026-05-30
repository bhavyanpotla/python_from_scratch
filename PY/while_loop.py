#syntax :
# while condition/expression:
# statement(s)
count = 1
while count<=4:
    print(count)
    count += 1
l = [1,2,5,0,7]
while l:
    print('hey,hi!')
    print(l.pop())  # hi chepta okoka element ni pop chestadhi

#while _ else block is not like the for_else here whenever the while is false then else is gonna execute

cou = 1
while cou<=5:
    print(cou)
    cou += 1
else:
    print('in else block')

coun = 1
while coun<=5:
    print(coun)
    coun += 1
    if coun == 3:
        break
else:
    print('in else block')
