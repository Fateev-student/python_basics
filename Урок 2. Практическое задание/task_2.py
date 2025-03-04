"""
Задание 2. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

Пример:
Введите целые числа через пробел: 1 2 3 4
Результат: 2 1 4 3

Введите целые числа через пробел: 1 2 3
Результат: 2 1 3
"""

def swap(some_list, pos1, pos2):
    some_list[pos1], some_list[pos2] = some_list[pos2], some_list[pos1]
    return some_list


num_list = list(map(int, input("Введите целые числа через пробел: ").strip().split()))

there_is_more_elements = True
i = 0
list_len = len(num_list)

while there_is_more_elements:
    swap(num_list, i, i + 1)
    i += 2
    if i + 1 >= list_len:
        there_is_more_elements = False

print(f"Результат: {num_list}")
