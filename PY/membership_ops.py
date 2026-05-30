# =========================
# MEMBERSHIP OPERATORS IN PYTHON
# =========================
# Membership operators are used to test
# whether a value exists inside a sequence or collection

# Operators:
# in      → returns True if value is present
# not in  → returns True if value is NOT present


# -------------------------
# MEMBERSHIP IN LIST
# -------------------------
nums = [10, 20, 30, 40, 50]

print(10 in nums)          # True
print(25 in nums)          # False
print(25 not in nums)      # True


# -------------------------
# MEMBERSHIP IN TUPLE
# -------------------------
tup = (1, 2, 3, 4)

print(3 in tup)            # True
print(5 in tup)            # False
print(5 not in tup)        # True


# -------------------------
# MEMBERSHIP IN SET
# -------------------------
# Sets are unordered but very FAST for membership testing

s = {5, 10, 15, 20}

print(10 in s)             # True
print(30 in s)             # False
print(30 not in s)         # True


# -------------------------
# MEMBERSHIP IN STRING
# -------------------------
# Checks for SUBSTRING or CHARACTER presence

name = "python"

print('p' in name)         # True
print('py' in name)        # True
print('thon' in name)      # True
print('x' in name)         # False
print('x' not in name)     # True


# -------------------------
# MEMBERSHIP IN DICTIONARY
# -------------------------
# IMPORTANT:
# Membership checks ONLY KEYS, not values

data = {'a': 10, 'b': 20, 'c': 30}

print('a' in data)         # True
print('z' in data)         # False
print(10 in data)          # False (checks keys, not values)

# To check values:
print(10 in data.values()) # True
print(40 in data.values()) # False


# -------------------------
# MEMBERSHIP WITH RANGE
# -------------------------
r = range(1, 10)

print(5 in r)              # True
print(10 in r)             # False
print(10 not in r)         # True


# =========================
# MEMBERSHIP vs INDEXING
# =========================
# Membership → checks existence
# Indexing → accesses value

lst = [100, 200, 300]

print(200 in lst)          # True
print(lst[1])              # 200

# error:: IndexError – index out of range
# print(lst[5])


# =========================
# QUIZ QUESTIONS (WITH REASON)
# =========================

# Q1
x = "hello"
print('h' in x)            # True

# REASON:
# 'h' is a character present in string "hello"


# Q2
d = {1: 'a', 2: 'b'}
print(1 in d)              # True

# REASON:
# Dictionary membership checks ONLY keys


# Q3
print('a' in d.values())   # True

# REASON:
# values() returns all values for membership testing


# =========================
# IMPORTANT REVISION POINTS
# =========================
# 1. in / not in are membership operators
# 2. Works with list, tuple, set, string, dict, range
# 3. Dictionary membership checks KEYS only
# 4. Sets are fastest for membership testing
# 5. Strings check characters or substrings
# 6. Membership returns BOOLEAN (True / False)
