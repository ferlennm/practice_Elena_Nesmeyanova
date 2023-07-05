L = int(input()) #считываем длину текста
text = input() #считываем текст и сохраняем его в переменную text

words = text.split() #разделяем текст на слова

the_longest_word = words[0] #инициализируем самое длинное слово первым словом из списка
length_longest_word = len(the_longest_word) #инициализируем длину самого длинного слова длиной первого слова

for word in words:
    if len(word) > length_longest_word: #если длина текущего слова больше длины самого длинного слова,то
        the_longest_word = word         #обновляем самое длинное слово
        length_longest_word = len(the_longest_word) #обновляем длину самого длинного слова

print(the_longest_word) #выводим самое длинное слово
print(length_longest_word) #выводим его длину
