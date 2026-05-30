# =========================
# OPERATORS IN PYTHON
# =========================

# -------------------------
# ARITHMETIC OPERATORS
# -------------------------
a = 3
b = 2

print(a + b)          # 5   (addition)
print(a - b)          # 1   (subtraction)
print(a * b)          # 6   (multiplication)
print(a / b)          # 1.5 (true division)
print(a // b)         # 1   (floor division)
print(a % b)          # 1   (modulus / remainder)


# -------------------------
# ASSIGNMENT OPERATORS
# -------------------------
a = a + 2
print(a)              # 5

b += 3
print(b)              # 5

print(a == b)         # True  (comparison)

a += 2
print(a)              # 7

# error:: ++ operator does NOT exist in Python (it is from C/C++)
# a++


# -------------------------
# MULTIPLE ASSIGNMENT
# -------------------------
v, w = 6, 5
print(v)              # 6
print(w)              # 5


# -------------------------
# UNARY OPERATOR
# -------------------------
# Unary operator works on ONE operand

print(-a)             # -7

# error:: incomplete expression
# a-

# Unary minus
a = -8
print(a)              # -8
print(-a)             # 8

# NOTE:
# -a → unary operator
# a - b → binary operator


# -------------------------
# RELATIONAL (COMPARISON) OPERATORS
# -------------------------
a, b = 4, 3

print(a > b)          # True
print(a < b)          # False
print(a <= b)         # False

b = 4
print(a <= b)         # True
print(a < b)          # False
print(a >= b)         # True
print(a > b)          # False
print(a == b)         # True
print(a != b)         # False

# NOTE:
# =  → assignment
# == → comparison


# -------------------------
# LOGICAL OPERATORS
# -------------------------
print(a < 10)         # True
print(b > 1)          # True

# error:: && is NOT valid in Python (used in C/C++)
# a < 10 && b > 1

# error:: & is bitwise AND, not logical AND
print(a < 10 & b > 1) # False (wrong logic)

# Correct logical operators
print(a < 10 and b > 1)   # True
print(a < 10 or b > 1)    # True
print(a < 10 or b > 10)   # True
print(a < 10 and b > 10)  # False


# -------------------------
# NOT OPERATOR
# -------------------------
result = True
print(result)         # True
print(not result)     # False


# =========================
# QUIZ QUESTION (WITH REASON)
# =========================
a, b = 3, 4

a *= 2                # a = a * 2 → 6
b -= a                # b = b - a → 4 - 6 = -2

print(a)              # 6
print(b)              # -2




# =========================
# IMPORTANT REVISION POINTS
# =========================
# 1. Python has NO ++ or -- operators
# 2. / always returns float
# 3. // removes decimal part
# 4. Unary operators need only one operand
# 5. Use and / or / not for logical operations
# 6. & | ^ are BITWISE operators, not logical
# 7. Assignment operators modify variable in-place
