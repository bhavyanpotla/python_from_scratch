# =========================
# LIST CREATION[list is a sequence data type and a dynamic storage array]
# =========================
 
numbers = [45, 87, 21, 24, 99]
print(numbers)                           # [45, 87, 21, 24, 99]


# =========================
# LIST INDEXING
# =========================
# Lists use 0-based indexing

print(numbers[0])                        # 45

# print(numbers[5])
# error:: IndexError – index 5 does not exist (valid indexes: 0 to 4)
 

print(numbers[4])                        # 99
print(numbers[-1])                       # 99  (negative index starts from end)


# =========================
# LIST SLICING
# =========================
# slicing format → list[start : end-1]

print(numbers[2:4])                      # [21, 24]
print(numbers[2:])                       # [21, 24, 99]


# =========================
# LIST OF STRINGS
# =========================
names = ['navin', 'harsh', 'kiran']
print(names)                             # ['navin', 'harsh', 'kiran']


# =========================
# MIXED DATA TYPE LIST
# =========================
mix = ['navin', 67, 6.53]
print(mix)                               # ['navin', 67, 6.53]


# =========================
# NESTED LIST (LIST INSIDE LIST)
# =========================
mix = [numbers, names]
print(mix)
# [[45, 87, 21, 24, 99], ['navin', 'harsh', 'kiran']]

print(mix[0])                            # [45, 87, 21, 24, 99]
print(len(mix))                          # 2  (number of inner lists)


# =========================
# ACCESSING ELEMENTS IN NESTED LIST
# =========================
# format → list[outer_index][inner_index]

print(mix[0][0])                         # 45
print(mix[1][2])                         # kiran


# =========================
# COMBINING LISTS (CONCATENATION)
# =========================
# + operator joins two lists into a single list

nums = [34, 54, 99, 74, 24]
print(nums)                              # [34, 54, 99, 74, 24]

print(names)                             # ['navin', 'harsh', 'kiran']

mix = nums + names
print(mix)
# [34, 54, 99, 74, 24, 'navin', 'harsh', 'kiran']
