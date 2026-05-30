'''
def f(l):
    res = []
    for i in l:
        if isinstance(i,list):
            res.extend(f(i))
        else:
            res.append(i)
    return res
print(f([1,2,3,[4,5,6,7,[8,9]],10]))
'''

