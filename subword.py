def word_count(word):
    count = 0
    for letter in word:
        count += 1
    return count

def find_longest_subword(word1, word2):
    for i in range(min(len(word1), len(word2)), 0, -1):
        if word1[-i:] == word2[:i]:
            return word2[:i]
    return None

first_w = input("First word: ")
second_w = input("Second word: ")

first_w_count = word_count(first_w)
second_w_count = word_count(second_w)

print(f"Length of the first word: {first_w_count}")
print("First word: " + first_w)
print(f"Length of the second word: {second_w_count}")
print("Second word: " + second_w)

subword = find_longest_subword(first_w, second_w)
if subword:
    print("Both words can be linked with the word " + subword + ".")
else:
    print("Both words cannot be linked.")