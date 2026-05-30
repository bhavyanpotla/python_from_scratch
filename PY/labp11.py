nums = [1, -2, 3, 0, 10]

unique_nums = list(set(nums))
 
unique_nums.remove(max(unique_nums))
second_largest = max(unique_nums)
 
unique_nums.remove(min(unique_nums))
second_smallest = min(unique_nums)

print(f"second_largest = {second_largest}")
print(f"second_smallest = {second_smallest}")
