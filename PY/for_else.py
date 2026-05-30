# this for_else loop is not just like normal if_else loop else here executes if only the total for loop executed without any interruption.
num = [23,6,7,45,-3,4,0,56,78]
for i in num:
    print(i)
else:
    print('sucessfully completed!')

# for example if i interrupt the loop then the else will'nt actually execute

nums = (12,4,56,97,6,-35,-64,0,92,19)
for i in nums:
    print(i)
    if i == 0:
        break
else:
    print('done! loop executed totally')
print('out of the for_else loop!')
