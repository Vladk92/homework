# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
# вычислите и выведите y

equation = 'y = -12x + 11111140.2121'
x = 2.5
line = equation.split(' ')
line_x = line[2][-1]                # извлекаем х
line_k = line[2][0:len(line[2])-1]  # извлекаем k
x_dict = {'x': x}                   # чтобы получить доступ к иксу
y = float(line_k) * float(x_dict[line_x]) + float(line[4])
print('y = ', y)
# Вась, вопрос к тебе, как быть, если вдруг в моих переменных
# line_x, line_k или x_dict[line_x] окажутся буквы, а не числа?