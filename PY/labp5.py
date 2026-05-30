def group_words(word_list):
    # 1. Khali dictionary create chestunnam
    groups = {}

    for word in word_list:
        # Handle empty strings (just in case)
        if not word:
            continue
            
        # 2. First letter ni Key ga teesukuntunnam
        first_char = word[0].upper()

        # 3. Aa letter ki box (list) lekapote, create chestam
        if first_char not in groups:
            groups[first_char] = []
        
        # 4. Final ga word ni aa list lo add (append) chestam
        groups[first_char].append(word)
        
    return groups

# Testing the code
my_words = ["apple", "banana", "apricot", "cherry", "blueberry", "avocado"]
result = group_words(my_words)

print("Grouped Words Dictionary:")
print(result)