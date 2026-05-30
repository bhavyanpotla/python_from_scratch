'''
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    shortened = list(set(lst))
    print(f'original list is {lst}')
    print(f'duplicates list is {list(duplicates)}')
    print(f'shortened list is {shortened}')

print(find_duplicates([12,34,12,34,45,54,3,57,3,5,1,2,5,1,90,99,45]))  
'''
'''
def max_in_tuples(tup):
    maximum = tup[0]
    for item in tup:
        if item > maximum:
            maximum = item
    return maximum
print(max_in_tuples((1,2,34,56,101,999)))
'''
'''
li = [12,13,14,15,16,17,90,89,900,1000]
print(li)
print(li[::-1])
def reverse_list(lst):
    lsts = []
    l=len(lst)-1
    while l >= 0:
        lsts.append(lst[l])
        l -= 1
    return lsts
print(reverse_list([12,13,14,15,16,17,90,89,900,1000]))
'''
'''
def duplicate_names(lst):
    tracker = set()
    duplicates = set()
    for item in lst:
        if item in tracker:
            duplicates.add(item)
        else:
            tracker.add(item)
    return list(tracker)
print(duplicate_names([
    "Alice", "Bob", "Charlie", "David", "Alice", 
    "Eve", "Frank", "Grace", "Bob", "Hannah", 
    "Ivan", "Charlie", "Jack", "Grace", "Kate"
]))
'''
def findpairs(lst,target):
    seen = set()
    pairs = []
    for num in lst:
        complement = target - num
        if complement in seen:
            pairs.append((complement,num))
        seen.add(num)
    return pairs
print(findpairs([2, 4, 3, 7, 5, 8, 1],9))
