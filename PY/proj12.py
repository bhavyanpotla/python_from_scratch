# FIZZ BUZZ INTERVIEW QSN
for i in range(1,101):
    if i%3 == 0:
        print('FIZZ')
    elif i%5 == 0:
        print('BUZZ')
    elif i%3 == 0 and i%5 == 0:
        print('FIZZ BUZZ')
    else:
        print(i)
