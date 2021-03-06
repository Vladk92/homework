# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
N = int(input('Введите номер квартиры: '))
if N < 1:
    print('Ты мудак? Как в башне может быть меньше одной квартиры?')
elif N > 2000000:
    print('Такая башня слишком велика даже для вавилонцев')
else:
    inc = 0         # для определения макроуровня (показывает, сколько квартир на данном этаже)
    count = 0       # номер верхней квартиры максимального макроуровня
    floors = 0      # всего этажей с первого до (inc - 1) макроуровня
    level = 0       # эта переменная покажет нам этаж
    position = 0    # эта переменная нам покажет позицию слева на этаже
    list_roof = []  # не знаю, как по-другому извлечь максимальный номер квартиры предыдущего макроуровня
    while count < N:
        inc += 1
        list_roof.append(count)
        count += inc ** 2
    for floor in range(inc):
        floors += floor
    if (N - list_roof[inc-1]) % inc == 0:
        level = floors + (N - list_roof[inc-1]) // inc
    else:
        level = floors + (N - list_roof[inc-1]) // inc + 1
    if (N - list_roof[inc-1]) % inc == 0:
        position = inc
    else:
        position = (N - list_roof[inc-1]) % inc
    print('этаж {}-й квартиры - {}, {}-ая слева'.format(N, level, position))
