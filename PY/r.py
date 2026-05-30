s='geetha charan has a versatile attitude !@'
words = s.split()
result = ""
for i in range(len(words)):
    reversed_word = words[i][::-1]
    result+=reversed_word

    if i<len(words) - 1:
        result+= " "

print(result)

