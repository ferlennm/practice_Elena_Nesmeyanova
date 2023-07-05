n = int(input()) #считываем число n (длину улицы)
strt = list(map(int, input().split())) #считываем список чисел

distances = [-1] * n #cоздаем список distances и заполняем его значениями -1
length = n

for i in range(n): #проходим по каждому элементу в списке strt
    if strt[i] == 0:        #если текущий элемент равен 0
        length = 0          #устанавливаем length как 0
    elif length != n:       #если length не равно n
        length += 1         #увеличиваем length на 1
    distances[i] = length   #присваиваем distances[i] значение length

length = n 

for i in range(n - 1, -1, -1): #проходим по каждому элементу в списке strt в обратном порядке
    if strt[i] == 0:             #если текущий элемент равен 0
        length = 0               #устанавливаем length как 0
    elif length != n:            #если length не равно n
        length += 1              #увеличиваем length на 1
    if distances[i] > length:    #если значение distances[i] больше length
        distances[i] = length    #присваиваем distances[i] значение length

print(" ".join(map(str, distances))) #выводим элементы списка distances через пробел
