# =========================
# PYTHON DATATYPES
# =========================

# -------------------------
# NUMERIC DATATYPES
# -------------------------
x = 10
print(type(x))                     # <class 'int'>

pi = 3.14
print(type(pi))                    # <class 'float'>

c = 6 + 8j
print(c)                           # (6+8j)
print(type(c))                     # <class 'complex'>

# NOTE:
# In mathematics imaginary unit is 'i'
# In Python imaginary unit is 'j'


# -------------------------
# COMPLEX NUMBER USING complex()
# -------------------------
a = 2
b = 3
c = complex(a, b)
print(c)                           # (2+3j)


# -------------------------
# TYPE CONVERSION (TYPE CASTING)
# -------------------------
k = int(pi)
print(k)                           # 3
# int() truncates decimal part, does NOT round

p = float(k)
print(p)                           # 3.0
print(type(p))                     # <class 'float'>


# -------------------------
# STRING DATATYPE
# -------------------------
name = 'navin'
print(type(name))                  # <class 'str'>


# -------------------------
# BOOLEAN DATATYPE
# -------------------------
f = 7
g = 6

greater = g > f
print(greater)                     # False

greater = g < f
print(greater)                     # True

is_it = True
print(is_it)                       # True

# error:: Python does NOT support ! for NOT
# !(is_it)

print(not is_it)                   # False


# -------------------------
# BOOLEAN AS INTEGERS
# -------------------------
k = int(True)
h = int(False)
print(k)                           # 1
print(h)                           # 0

# NOTE:
# True → 1
# False → 0


# -------------------------
# COLLECTION DATATYPES
# -------------------------
l = [4, 5, 6, 7]
print(type(l))                     # <class 'list'>

t = (4, 5, 6, 7)
print(type(t))                     # <class 'tuple'>

s = {4, 5, 6, 7}
print(type(s))                     # <class 'set'>


# -------------------------
# RANGE DATATYPE
# -------------------------
r = range(10)
print(r)                           # range(0, 10)
print(type(r))                     # <class 'range'>

print(list(r))                     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(set(r))                      # {0,1,2,3,4,5,6,7,8,9}
print(tuple(r))                    # (0,1,2,3,4,5,6,7,8,9)

# range(start, stop, step)
print(set(range(2, 11, 2)))        # {2, 4, 6, 8, 10}


# =========================
# QUIZ QUESTIONS (WITH REASONS)
# =========================

# Q1
ls = [4, 5, 6]
tup = (7, 8)

v = list(tup)
print(v)                           # [7, 8]

# REASON:
# list() converts tuple into list
# Tuples are immutable → conversion needed for modification


# Q2
tup = (1, 2, 3)
y = list(tup)

print(type(y))                     # <class 'list'>
print(y)                           # [1, 2, 3]

# REASON:
# list() always returns a LIST
# tuple → list conversion creates a NEW object


# =========================
# IMPORTANT REVISION POINTS
# =========================
# 1. Python supports int, float, complex
# 2. complex numbers use 'j'
# 3. int() truncates decimals
# 4. Boolean is subclass of int
# 5. not is logical NOT (not !)
# 6. list → mutable
# 7. tuple → immutable
# 8. set → unordered, unique values
# 9. range is memory-efficient sequence
# 10. list(), tuple(), set() are type converters
