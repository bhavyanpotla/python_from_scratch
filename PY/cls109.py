#check if a string is palindrome using the recursion
def palindrome(str):
    if len(str)<=1:
        return True
    if str[0].lower() != str[-1].lower():
        return False
    return palindrome(str[1:-1])
print(palindrome('madam'))
print(palindrome('hello'))
print(palindrome('malayalam'))
print(palindrome('j'))
