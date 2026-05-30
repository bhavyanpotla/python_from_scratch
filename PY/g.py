s="tomorrow is my python exam"
words = s.split()
total_words = len(words)
total_char_withspace = len(s)
total_char_withoutspace = len(s.replace(' ',''))
longest_word = max(words , key = len)

print(words)
print(total_words)
print(total_char_withspace)
print(total_char_withoutspace)
print(longest_word)
