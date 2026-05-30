def p(nums,k):

    for i in range(len(nums)):
        for j in range(0,len(nums)-i-1):
            if nums[j] < nums[j+1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    
    return nums[k-1]

print(p([12,83,3764,682,-129,0],6))
