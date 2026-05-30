# 0--tails
# 1--heads
print('*****Welcome to the virtual tossing coin game , play it and try you luck!*****')
print('lets toss the coin whats ur call ? 0.tails 1.heads')
call=int(input('enter (0/1):'))
import random
a=random.randint(0,1)
if a==0:
    print('tails is the result')
elif a==1:
    print('heads is the result')

if call==a:
    print('you won!')
else:
    print('sorry! u lost please try again!')
