# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

user_number_of_elements = int(input('Введите желаемое число элементов: '))
list_for_treatment = []

for element in range(user_number_of_elements):
    list_for_treatment.append(random.randint(0, 10))

print(f'Получен список чисел:\n{list_for_treatment}')
print()

sum_of_numbers_with_odd_indexes = 0
i = 1

while i < len(list_for_treatment):
    sum_of_numbers_with_odd_indexes = sum_of_numbers_with_odd_indexes + list_for_treatment[i]
    i += 2

print(f'Сумма элементов списка, стоящих на нечётной позиции равна: {sum_of_numbers_with_odd_indexes}')


# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

user_number_of_elements2 = int(input('Введите желаемое число элементов: '))
list_for_treatment2 = []

for element in range(user_number_of_elements2):
    list_for_treatment2.append(random.randint(0, 10))

print(f'Получен список чисел:\n{list_for_treatment2}')
print()

from_left_to_right_index = 0
from_right_to_left_index = -1
result_list = []

while from_left_to_right_index <= round((len(list_for_treatment2) + 0.1) / 2) and - from_right_to_left_index <= round((len(list_for_treatment2) + 0.1) / 2):
    result_list.append(list_for_treatment2[from_left_to_right_index] * list_for_treatment2[from_right_to_left_index])
    from_left_to_right_index += 1
    from_right_to_left_index += -1

print(f'Попарно перемножены элементы вводного списка, получен итоговый список:\n{result_list}')

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

user_number_of_elements3 = int(input('Введите желаемое число элементов: '))
list_for_treatment3 = []

for element in range(user_number_of_elements3):
    list_for_treatment3.append(random.randint(0,10) + round(random.random(), 2))

print(f'Получен список чисел:\n{list_for_treatment3}')

list_for_treatment3_without_whole_part = []

for element in list_for_treatment3:
    list_for_treatment3_without_whole_part.append(element - int(element))

result = max(list_for_treatment3_without_whole_part) - min(list_for_treatment3_without_whole_part)

print(f'Разница между максимальным и минимальным значением дробной части элементов равна: {result}')

# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

user_number = int(input("Введите число: "))
binary_result = []

while user_number:
    binary_result.append(user_number % 2)
    user_number //= 2
binary_result.reverse()
print(binary_result)

