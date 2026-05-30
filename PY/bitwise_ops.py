# =========================
# BITWISE OPERATORS IN PYTHON
# =========================
# Bitwise operators work at the BINARY (bit) level
# They operate on 0s and 1s, not on boolean logic

# Binary reference:
# 5  → 0101
# 3  → 0011
# 6  → 0110
# 1  → 0001


# -------------------------
# BITWISE AND (&)
# -------------------------
# Result bit is 1 only if BOTH bits are 1

print(5 & 3)          # 1   → 0101 & 0011 = 0001
print(6 & 3)          # 2   → 0110 & 0011 = 0010
print(8 & 1)          # 0   → 1000 & 0001 = 0000


# -------------------------
# BITWISE OR (|)
# -------------------------
# Result bit is 1 if ANY one bit is 1

print(5 | 3)          # 7   → 0101 | 0011 = 0111
print(6 | 3)          # 7   → 0110 | 0011 = 0111
print(8 | 1)          # 9   → 1000 | 0001 = 1001


# -------------------------
# BITWISE XOR (^)
# -------------------------
# Result bit is 1 if bits are DIFFERENT

print(5 ^ 3)          # 6   → 0101 ^ 0011 = 0110
print(6 ^ 3)          # 5   → 0110 ^ 0011 = 0101
print(9 ^ 9)          # 0   → same bits cancel out


# -------------------------
# BITWISE NOT (~)
# -------------------------
# Inverts all bits (uses 2's complement)

print(~5)             # -6
print(~0)             # -1
print(~(-1))          # 0

# NOTE:
# ~x = -(x + 1)
# Example: ~5 = -(5+1) = -6


# -------------------------
# LEFT SHIFT (<<)
# -------------------------
# Shifts bits LEFT and adds 0s on the right
# Effectively multiplies by 2^n

print(5 << 1)         # 10  → 0101 << 1 = 1010
print(5 << 2)         # 20  → 0101 << 2 = 10100
print(3 << 3)         # 24  → 0011 << 3 = 11000


# -------------------------
# RIGHT SHIFT (>>)
# -------------------------
# Shifts bits RIGHT
# Effectively divides by 2^n (floor division)

print(10 >> 1)        # 5   → 1010 >> 1 = 0101
print(20 >> 2)        # 5   → 10100 >> 2 = 00101
print(8 >> 3)         # 1   → 1000 >> 3 = 0001


# =========================
# BITWISE vs LOGICAL (IMPORTANT)
# =========================
a = 4
b = 3

print(a & b)          # 0   (bitwise AND)
print(a and b)        # 3   (logical AND)

print(a | b)          # 7   (bitwise OR)
print(a or b)         # 4   (logical OR)

# NOTE:
# Bitwise → works on bits
# Logical → works on truth values


# =========================
# COMMON EXAM TRAPS
# =========================
# 1. & | ^ are NOT logical operators
# 2. Use and / or / not for conditions
# 3. XOR (^) returns 0 when values are same
# 4. Left shift multiplies, right shift divides
# 5. ~ operator gives negative result due to 2's complement
