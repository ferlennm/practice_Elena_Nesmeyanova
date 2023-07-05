s = input() #считываем строку s
t = input() #считываем строку t

letter_count = {} #создаем пустой словарь для подсчета количества каждой буквы

for letter in s: #проходим по каждой букве в строке s
    if letter in letter_count:       #если буква уже есть в словаре
        letter_count[letter] += 1    #увеличиваем счетчик для этой буквы на 1
    else:                            
        letter_count[letter] = 1     #иначе инициализируем счетчик для этой буквы с 1

for letter in t: #проходим по каждой букве в строке t
    if letter in letter_count:       #если буква есть в словаре
        letter_count[letter] -= 1    #уменьшаем счетчик для этой буквы на 1
    else:
        letter_count[letter] = 1     #иначе инициализируем счетчик для этой буквы с 1

for letter in letter_count: #проходим по каждой букве в словаре
    if letter_count[letter] != 0: #если счетчик для буквы не равен 0
        extra_letter = letter     #записываем эту букву как лишнюю

print(extra_letter) #выводим лишнюю букву
