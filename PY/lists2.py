# =========================
# LIST CREATION
# =========================
n = [23, 56, 14, 36, 45]
nm = ['navin', 'harsh', 'kiran']

mix = [n, nm]
print(mix)
# [[23, 56, 14, 36, 45], ['navin', 'harsh', 'kiran']]


# =========================
# LIST CONCATENATION
# =========================
# + combines two lists into a single list

mix = n + nm
print(mix)
# [23, 56, 14, 36, 45, 'navin', 'harsh', 'kiran']


# =========================
# APPEND (adds ONE element at the end)
# =========================
n.append(33)
print(n)
# [23, 56, 14, 36, 45, 33]


# =========================
# COUNT (counts occurrences)
# =========================
print(n.count(14))        # 1
print(n.count(15))        # 0


# =========================
# INSERT (insert at specific index)
# =========================
n.insert(1, 55)
print(n)
# [23, 55, 56, 14, 36, 45, 33]


# =========================
# REMOVE (removes FIRST matching value)
# =========================
n.remove(56)
print(n)
# [23, 55, 14, 36, 45, 33]


# =========================
# POP (removes element using index)
# =========================
print(n.pop(4))           # 45
print(n)
# [23, 55, 14, 36, 33]


# =========================
# STACK CONCEPT (LAST INPUTTED WILL BE FIRST OUTED)
# =========================
# pop() without index removes LAST element

print(n.pop())            # 33
print(n)
# [23, 55, 14, 36]


# =========================
# DELETE USING SLICING
# =========================
del n[2:4]
print(n)
# [23, 55]


# =========================
# EXTEND (adds MULTIPLE elements)
# =========================
# [23, 55, 14, 36]
n.extend([44, 56, 11, 99])
print(n)
# [23, 55, 44, 56, 11, 99]


# =========================
# REPLACING ELEMENTS USING SLICING
# =========================
n[2:4] = [54, 76] 
print(n)
# [23, 55, 54, 76, 11, 99]


# =========================
# REVERSE (in-place)
# =========================
n.reverse()
print(n)
# [99, 11, 76, 54, 55, 23]


# =========================
# SORT (ascending order)
# =========================
n.sort()
print(n)
# [11, 23, 54, 55, 76, 99]


# =========================
# BUILT-IN FUNCTIONS ON LISTS
# =========================
print(min(n))             # 11
print(max(n))             # 99
print(sum(n))             # 318


# =========================
# MIN & MAX ON STRING LIST
# =========================
# works based on alphabetical (ASCII) order

print(min(nm))            # harsh
print(max(nm))            # navin

# error:: sum() not supported for string list
# print(sum(nm))

