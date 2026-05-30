# =========================
# DICTIONARY CREATION
# =========================
# Dictionary stores data as key : value pairs
# Keys must be UNIQUE and IMMUTABLE

data = {0: 34, 1: 35, 2: 67, 3: 8}
print(data[2])                         # 67

# =========================
# DICTIONARY WITH STRING KEYS
# =========================
data = {'kiran': 34, 'sushil': 35, 'harsh': 67, 'navin': 8}

# error:: KeyError – key 1 does not exist
# print(data[1])

print(data['navin'])                   # 8
print(data['harsh'])                   # 67
print(type(data))                      # <class 'dict'>


# =========================
# get() METHOD
# =========================
# get() returns None (or default value) instead of error

print(data.get('harsh'))               # 67
print(data.get(1))                     # None
print(data.get('kiran', 'not found'))  # 34
print(data.get('1', 'not found'))      # not found


# =========================
# DUPLICATE KEYS
# =========================
# If duplicate keys exist, LAST value is retained

data = {'kiran': 34, 'sushil': 35, 'harsh': 67, 'navin': 8, 'harsh': 34}
print(data)
# {'kiran': 34, 'sushil': 35, 'harsh': 34, 'navin': 8}

print(data.get('34', 'not found'))     # not found
print(data.get('harsh', 'not found'))  # 34


# =========================
# CREATING DICTIONARY USING zip()
# =========================
# zip() pairs elements position-wise

keys = {'abc', 'def', 'ghi'}
values = [23, 46, 75]

dict1 = dict(zip(keys, values))
print(dict1)
# {'ghi': 23, 'def': 46, 'abc': 75}
# (order may vary because sets are unordered)


# =========================
# REMOVING ELEMENTS
# =========================
print(data.pop('navin'))               # 8
print(data)
# {'kiran': 34, 'sushil': 35, 'harsh': 34}

del data['sushil']
print(data)
# {'kiran': 34, 'harsh': 34}


# =========================
# NESTED DATA STRUCTURES
# =========================
# Dictionary can contain list, set, tuple, or another dictionary

data = {
    'js': 'vscode',
    'python': ['vscode', 'pycharm'],
    'java': {'core': 'vscode', 'spring': 'iij'}
}

print(data)
# {'js': 'vscode', 'python': ['vscode', 'pycharm'], 'java': {'core': 'vscode', 'spring': 'iij'}}


# =========================
# ACCESSING NESTED DATA
# =========================
print(data['js'])                      # vscode
print(data['java'])                    # {'core': 'vscode', 'spring': 'iij'}
print(data['python'])                  # ['vscode', 'pycharm']

print(data['python'][0])               # vscode

# error:: IndexError – list index out of range
# print(data['python'][2])

print(data['python'][1])               # pycharm
print(data['java']['core'])            # vscode
print(data['java']['spring'])          # iij


# =========================
# KEY REVISION POINTS
# =========================
# 1. Dictionary = key : value pairs
# 2. Keys must be UNIQUE
# 3. Accessing missing key → KeyError
# 4. get() is safer than []
# 5. Duplicate keys overwrite previous values
# 6. Dictionary can contain list, set, tuple, or dict inside it
