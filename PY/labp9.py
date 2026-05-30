def rev(s):
    if len(s)<=1:
        return s
    return rev(s[1:]) + s[0]
string = "tanvi"
print(f'org = {string}')
print(f'rev = {rev(string)}')
 