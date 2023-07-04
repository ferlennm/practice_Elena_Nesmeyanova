s = input()
t = input()

letter_count = {}

for letter in s:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

for letter in t:
    if letter in letter_count:
        letter_count[letter] -= 1
    else:
        letter_count[letter] = 1

for letter in letter_count:
    if letter_count[letter] != 0:
        extra_letter = letter

print(extra_letter)