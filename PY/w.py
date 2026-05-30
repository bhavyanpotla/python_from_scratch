arr = [1,2,3,-2,5]
target = 5

for i in range(len(arr)):
    sum = 0
    for j in range(i,len(arr)):
        sum+=arr[j]
        if sum == target:
            print(arr[i:j+1])
        
