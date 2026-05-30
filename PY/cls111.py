'''
#string as an input and find all the substring in it

def f(s):
    n = len(s)
     
    for i in range(n):
        for j in range(i+1,n+1):
            print(s[i:j])
             
text = input('enter the main string:')
print(f(text))
'''
def k(s,start = 0,end = 1):
    if start == len(s):
        return  
    if end>len(s):
        (k(s,start+1,start+2))
        return
    print(s[start:end])
    k(s,start,end+1)
t = input('enter the string:')
print(k(t))

