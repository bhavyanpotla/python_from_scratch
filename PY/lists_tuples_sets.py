# ============================================================
# PYTHON LISTS, TUPLES, SETS — COMPLETE REVISION (Q&A STYLE)
# Author: Bhavyan (revision notes)
# ============================================================


# -----------------------------
# LIST QUESTIONS & ANSWERS
# -----------------------------

# Q1) What happens when two variables refer to the same list?
x = [10, 20, 30]
y = x
y.append(40)
print(x)
# ANSWER: [10, 20, 30, 40]
# Reason: x and y refer to the same list object (no copy created)


# Q2) How to copy a list properly?
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a, b)
# ANSWER: a = [1, 2, 3], b = [1, 2, 3, 4]


# Q3) Get only odd-position elements WITHOUT if
nums = [1, 2, 3, 4, 5, 6]
result = nums[::2]
print(result)
# ANSWER: [1, 3, 5]


# Q4) Remove duplicates from a list
data = [1, 2, 2, 3, 3, 3]
unique = list(set(data))
print(unique)
# ANSWER: [1, 2, 3] (order not guaranteed)


# -----------------------------
# TUPLE QUESTIONS & ANSWERS
# -----------------------------

# Q5) Why is this NOT a tuple?
t1 = (10)
print(type(t1))
# ANSWER: <class 'int'>
# Reason: parentheses alone do not make a tuple


# Q6) Correct single-element tuple
t2 = (10,)
print(type(t2))
# ANSWER: <class 'tuple'>


# Q7) Tuple unpacking
t3 = (100, 200, 300)
a, b, c = t3
print(b)
# ANSWER: 200


# Q8) Why are tuples faster than lists?
# ANSWER:
# Tuples are immutable, so Python does not allocate extra memory for changes.


# Q9) Can this tuple be added to a set?
t4 = (1, 2, (3, 4))
s1 = {t4}
print(s1)
# ANSWER: YES
# Reason: all elements inside the tuple are hashable


# Q10) Why this tuple CANNOT be added to a set?
t5 = (1, 2, [3, 4])
# s2 = {t5}   # ❌ ERROR
# ANSWER:
# A tuple is hashable only if ALL its elements are hashable.
# List inside tuple makes it unhashable.


# -----------------------------
# SET QUESTIONS & ANSWERS
# -----------------------------

# Q11) Do sets store duplicates?
s = {1, 2, 2, 3, 3}
print(s)
# ANSWER: {1, 2, 3}


# Q12) Membership test in set
print(2 in {1, 2, 3})
# ANSWER: True


# Q13) Set equality ignores order
A = {1, 2, 3}
B = {3, 2, 1}
print(A == B)
# ANSWER: True


# Q14) Add tuple to set
s3 = {1, 2}
s3.add((4, 5))
print(s3)
# ANSWER: {1, 2, (4, 5)}


# Q15) Why list cannot be added to a set?
# ANSWER:
# Lists are mutable and not hashable.


# Q16) Length of a set with duplicates
print(len({1, 2, 2, 3, 3, 3}))
# ANSWER: 3


# -----------------------------
# DICT & SET CONFUSION
# -----------------------------

# Q17) Is this a set?
x = {}
print(type(x))
# ANSWER: <class 'dict'>


# Q18) Correct empty set
empty_set = set()
print(type(empty_set))
# ANSWER: <class 'set'>


# -----------------------------
# INTERVIEW GOLDEN RULES
# -----------------------------

# 1) List  -> ordered, mutable, duplicates allowed
# 2) Tuple -> ordered, immutable, faster
# 3) Set   -> unordered, unique, fast lookup
# 4) Dict keys / Set elements must be HASHABLE
# 5) Tuple is hashable ONLY if all elements inside are hashable

# Mistakes I fixed (Lists / Tuples / Sets)

f=[1,2,3]; g=tuple(f); h=set(g)        # types → list, tuple, set
print(type(f),type(g),type(h))

print(len({1,2,2,3,3}))                # → 3 (set removes duplicates)

d={(1,2):"ok"}                         # tuple can be dict key
# d={[1,2]:"no"}                       # ❌ list not allowed

t=(1,2,[3,4])                          # ❌ not hashable → can't be in set
# set({t})

st={}                                   # {} is dict
es=set()                               # empty set

# -----------------------------
# END OF REVISION FILE
# -----------------------------

