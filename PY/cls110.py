def count_vowels(s):
    vowels = 'aeiouAEIOU'

    if len(s) == 0:
        return 0
    if s[0]  in vowels :
        return 1 + count_vowels(s[1:])
    else:
        return count_vowels(s[1:])
str = input('enter the string')
print(f'no of vowels : {count_vowels(str)}')

