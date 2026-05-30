# =========================
# SET CREATION
# =========================
# Sets store UNIQUE elements only (duplicates removed automatically)
# Sets are UNORDERED (no fixed index positions)

set1 = {23, 56, 78, 21, 56}
print(set1)
# {56, 21, 78, 23}   *random order


# =========================
# INDEXING NOT ALLOWED IN SET
# =========================
# error:: TypeError – sets are unordered, indexing not supported
# print(set1[1])

# error:: SyntaxError – invalid syntax
# set{1}


# =========================
# MEMBERSHIP OPERATOR (in)
# =========================
print(21 in set1)              # True

# error:: NameError – variable ste1 does not exist
# print(23 in ste1)

print(23 in set1)              # True
print(22 in set1)              # False


# =========================
# LENGTH & TYPE
# =========================
print(len(set1))               # 4
print(type(set1))              # <class 'set'>


# =========================
# EMPTY SET CREATION
# =========================
set2 = {}
print(type(set2))              # <class 'dict'>  (NOT a set!)

# Correct way to create empty set
set2 = set()
print(set2)                    # set()
print(type(set2))              # <class 'set'>


# =========================
# SET FROM STRING
# =========================
# Each character becomes a set element (duplicates removed)

set2 = set('abcdmnop')
print(set2)
# {'m', 'a', 'n', 'b', 'd', 'c', 'o', 'p'}  *random order

set3 = set('aeioupd')
print(set3)
# {'a', 'i', 'd', 'e', 'o', 'p', 'u'} *random order


# =========================
# SET DIFFERENCE (-)
# =========================
# Removes elements of set3 from set2
# Original sets remain unchanged

print(set2 - set3)
# {'m', 'n', 'c', 'b'}    *random order


# =========================
# SET UNION (|)
# =========================
# Combines all elements from both sets (no duplicates)

print(set2 | set3)
# {'m', 'a', 'n', 'b', 'i', 'd', 'c', 'e', 'o', 'p', 'u'}    *random order


# =========================
# SET INTERSECTION (&)
# =========================
# Prints only COMMON elements

print(set2 & set3)
# {'a', 'p', 'd', 'o'}     *random order


# =========================
# SET SYMMETRIC DIFFERENCE (^)
# =========================
# Prints NON-COMMON elements from both sets
# ^ is called caret operator

print(set2 ^ set3)
# {'b', 'c', 'e', 'm', 'n', 'i', 'u'}     *random order

#================================
#INBUILT FUNCTIONS USAGE IN SETS
#================================
SET={18,29,36,48,'bhavyan',True,1,0}
SET.add(99)
print(SET)
SET.remove(99)
print(SET)
print(SET.pop())   #here in sets pop removes random element not the last one!
print(SET)

#================================
# OPERATIONS IN SETS
#================================

s1={'nobitha','gian','suniyo'}
s2={'shizuka','nobitha','dekisuki'}
#UNION
print(s1 | s2)                                      #{'nobitha', 'dekisuki', 'shizuka', 'gian', 'suniyo'}
print(s1.union(s2))                                 #{'nobitha', 'dekisuki', 'shizuka', 'gian', 'suniyo'}
#print(s1 | ('doraemon') | ('doraeme'))             TypeError: unsupported operand type(s) for |: 'set' and 'str'
print(s1.union(('doraemon','doraeme')))             #{'doraeme', 'suniyo', 'gian', 'nobitha', 'doraemon'}
#INTERSECTION
print(s1 & s2)                                      #{'nobitha'}
print(s1.intersection(s2))                          #{'nobitha'}
#DIFFERENCE
print(s1 - s2)                                      #{'gian', 'suniyo'}
print(s1.difference(s2))                            #{'gian', 'suniyo'}
print(s1 ^ s2)                                      #{'suniyo', 'dekisuki', 'shizuka', 'gian'}
print(s1.symmetric_difference(s2))                  #{'suniyo', 'dekisuki', 'shizuka', 'gian'}
#ADDITIONAL OPERATORS
s3={ 1,2,3,4,5,-6,-7,-8,-9,29,47}
s4={ 29,-9,3,5,-7}
#DISJOINT SETS
print(s3.isdisjoint(s4))                            #False
#SUBSETS(<=)
print(s4.issubset(s3))                              #True
print(s4<=s3)                                       #True
#SUPERSETS(>=)
print(s3.issuperset(s4))                            #True
print(s3>=s4)                                       #True
# =========================
# KEY REVISION POINTS
# =========================
# 1. Sets store UNIQUE values
# 2. Sets are UNORDERED → no indexing
# 3. Fast membership checking using "in"
# 4. {} creates a dictionary, not a set
# 5. Use set() to create empty set
# 6. -, |, &, ^ are important EXAM OPERATORS
