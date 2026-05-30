k = 'this is a python programming class'
words = k.split()  # split into list of words
capitalized_words = []

for word in words:
    if word:  # check if word is not empty
        capitalized = word[0].upper() + word[1:]
        capitalized_words.append(capitalized)

result = ' '.join(capitalized_words)
print(result) 

