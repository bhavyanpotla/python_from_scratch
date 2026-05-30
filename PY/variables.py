# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#       VARIABLE STORAGE IN PYTHON
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# =========================
# OBJECT ID & MEMORY
# =========================
# id() returns the memory identity of an object (CPython implementation detail)

a = 5
b = 5

print(id(a))                      # same address
print(id(b))                      # same address

# Small integers are INTERNED (cached) in Python
# Usually from -5 to 256 (implementation dependent)


# =========================
# REASSIGNMENT CREATES NEW OBJECT
# =========================
b = 9
print(b)                          # 9
print(id(b))                      # different address


# =========================
# INTEGER INTERNING
# =========================
k = 5
print(k)                          # 5
print(id(k))                      # same as id(a)

b = 5
print(id(b))                      # same as id(a) and id(k)

# Old object (9) becomes unreferenced
# Python's garbage collector can reclaim it later


# =========================
# STRING INTERNING (SMALL STRINGS)
# =========================
name = 'navin'
name1 = 'navin'

print(id(name))                   # same address
print(id(name1))                  # same address
print(id(name) == id(name1))      # True

# This is called STRING INTERNING
# Python uses a string pool for small / identifier-like strings


# =========================
# LARGE STRINGS (NO INTERNING)
# =========================
s1 = 'My fav color is orange'
s2 = 'My fav color is orange'

print(id(s1))                     # different
print(id(s2))                     # different
print(id(s1) == id(s2))           # False

# Reason:
# Python avoids interning large strings to save memory
# Only small & reusable strings go into the string pool


# =========================
# LARGE INTEGERS (NO INTERNING)
# =========================
d = 1000
e = 1000

print(id(d) == id(e))             # False

# Small integers are cached
# Large integers usually create separate objects


# =========================
# QUIZ / TRICK QUESTION
# =========================
task = 'telusko'
task1 = 'telusko'

print(task)                       # telusko
print(task1)                      # telusko
print(id(task) == id(task1))      # True

# Reason:
# 'telusko' is a small string → INTERNED


# =========================
# IMPORTANT REVISION POINTS
# =========================
# 1. Variables do NOT store values — they reference objects
# 2. id() shows object identity, not exact RAM address
# 3. Integers & strings are IMMUTABLE
# 4. Small integers are cached (interned)
# 5. Small strings are interned using string pool
# 6. Large strings & large integers usually get new objects
# 7. Reassignment never modifies object — it changes reference
# 8. Unreferenced objects are handled by garbage collector
