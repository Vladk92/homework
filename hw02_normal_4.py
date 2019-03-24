# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

list_1 = [1, 1, 4, 3, 3, 7, 2, 2, 4, 5, 6, 2, 5, 2, 3, 4, 9, 8, 9]
# сначала решение б)
list_2 = []
for number in list_1:
    if list_1.count(number) == 1:
        list_2.append(number)
print(list_2)
# затем решение а)
list_3 = []
inc = 0  # для поиска по элементам list_1
inc_1 = 0  # вспомогательный инкремент, чтобы понять, все ли элементы list_3 не равны текущему элементы из list_1
element = 0
while inc < len(list_1):
    element = list_1[inc]
    for number in list_3:
        if element != number:
            inc_1 += 1
    if inc_1 == len(list_3):
        list_3.append(element)
    inc_1 = 0
    inc += 1
print(list_3)