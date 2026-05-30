# =========================
# TUPLE CREATION & TYPE 
# =========================


#(Tuples are faster because they are immutable.)
#(so Python doesn’t need to allocate extra memory for changes)

tup = [23, 45, 67, 43]
print(type(tup))                      # <class 'list'>

# Tuple without brackets (comma makes it a tuple)
tup = 23, 45, 67, 43
print(type(tup))                      # <class 'tuple'>

# Tuple with brackets (recommended)
tup = (23, 45, 67, 43)
print(tup)                            # (23, 45, 67, 43)


# =========================
# BUILT-IN FUNCTIONS ON TUPLE
# =========================
print(max(tup))                       # 67
print(min(tup))                       # 23


# =========================
# TUPLE vs LIST (IMMUTABILITY)
# =========================
# List → mutable (can change)
# Tuple → immutable (cannot change)

print(tup[2])                         # 67

# error:: TypeError – tuple does not support item assignment
# tup[2] = 65

print(len(tup))                       # 4


# =========================
# MIXED DATA TYPE TUPLE
# =========================
tupA = (2, 'cherry', 7.9)
print(type(tupA))                     # <class 'tuple'>


# =========================
# TUPLE UNPACKING
# =========================
# Values are assigned position-wise

n, nm, n1 = tupA

# error:: NameError – variable name is n, not num
# print(num)

print(n)                              # 2
print(nm)                             # cherry
print(n1)                             # 7.9


# =========================
# LIST INSIDE TUPLE
# =========================
# Tuple itself is immutable
# But mutable objects inside it CAN be changed

tupB = (34, 'navin', [3, 4, 5, 6])

# error:: TypeError – cannot modify tuple element
# tupB[0] = 34

# Modifying list inside tuple (allowed)
tupB[2][1] = 9
print(tupB)                           # (34, 'navin', [3, 9, 5, 6])


# =========================
# MEMBERSHIP OPERATOR (in)
# =========================
print(34 in tupB)                     # True

# error:: NameError – navin must be a string
# print(navin in tupB)

print('navin' in tupB)                # True
print('cherry' in tupA)               # True


# =========================
# FLOAT COMPARISON IN TUPLES
# =========================
# Floating-point values are stored approximately

print(7.90 in tupA)                   # True
print(7.90000 in tupA)                # True
print(7.9 in tupA)                    # True
print(7.90000000000000000 in tupA)    # True
print(7.9000000000000000001 in tupA)  # True
print(7.9001 in tupA)                 # False


# =========================
# KEY TAKEAWAY
# =========================
# Tuple is IMMUTABLE:
# - Cannot add, remove, or replace elements
# - But mutable objects (like lists) inside a tuple CAN be modified
