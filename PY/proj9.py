"""
# program to calculate average height from a list of heights
# heights_list = [1.7 1.6 1.5 1.4 1.3 1.9 1.8 1.7 1.8 2.0 1.5 1.5 1.5]
# print(f' average height:{sum(heights_list)/len(heights_list)} meters')

BUT WE WANNA MAKE A PROJECT WITHOUT THE SUM AND LEN BY USING THE (FOR)

"""

height = input('enter the heights of various persons(seperated by space) in meters:')
ht_list = height.split()
count = 0
for i in ht_list:
    count = count+1
print(f'length of the list is {count}')
for i in range(count):
    ht_list[i]=int(ht_list[i])

print(ht_list)
sum=0
for i in ht_list:
    sum=sum+i
print(f'the average of the heights is:{round(sum/count)}')

