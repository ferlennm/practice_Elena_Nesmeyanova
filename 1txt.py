L = int(input())
text = input()

words = text.split()

the_longest_word = words[0]
length_longest_word = len(the_longest_word)

for word in words:
    if len(word) > length_longest_word:
        the_longest_word = word
        length_longest_word = len(the_longest_word)

print(the_longest_word)
print(length_longest_word)
