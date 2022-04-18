from random import *
import datetime

def insert(data):
    for i in range(len(data)):
        j = i - 1
        key = data[i]
        while data[j] > key and j >= 0:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            """ Сравниваем первые элементы в начале каждого списка
             Если первый элемент левого подсписка меньше, добавляем его
             в отсортированный массив"""
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1

            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # Если достигнут конец левого списка, элементы правого списка добавляем в конец результирующего списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1

        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

def merge_sort(nums):
    # Возвращаем список, если он состоит из одного элемента
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    # Сортируем и объединяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)

def copy1(A):
    A1 = A[:]
    return A1

array = []
NoSort = []
Sort = []
PartSort = []
N = 10000


#Заполнение массива
for i in range(N):
    array.append(randint(-50, 20))


#Извлечение отрицательных
for i in range(len(array)):
    if array[i] < 0:
        NoSort.append(array[i])
        array[i] = None

#Сортировка + время выполнения
Sort = sorted(NoSort)
PartSort = sorted(NoSort[:len(NoSort) // 2])+ NoSort[len(NoSort)// 2 :]
ReSort  = Sort[::-1]

a = datetime.datetime.now()
insert(copy1(ReSort))
b = datetime.datetime.now()
ins1 = str((b - a).total_seconds())
print(f'Отсортированный в обратном вставками = {ins1}')

a = datetime.datetime.now()
insert(copy1(Sort))
b = datetime.datetime.now()
ins2 = str((b - a).total_seconds())
print(f'Отсортированный вставками = {ins2}')

a = datetime.datetime.now()
insert(copy1(PartSort))
b = datetime.datetime.now()
ins3 = str((b - a).total_seconds())
print(f'Частично отсортированный вставками = {ins3}')

a = datetime.datetime.now()
merge_sort(copy1(ReSort))
b = datetime.datetime.now()
mer1 = str((b - a).total_seconds())
print(f'Отсортированный в обратном слиянием = {mer1}')

a = datetime.datetime.now()
merge_sort(copy1(Sort))
b = datetime.datetime.now()
mer2 = str((b - a).total_seconds())
print(f'Отсортированный слиянием = {mer2}')

a = datetime.datetime.now()
merge_sort(copy1(PartSort))
b = datetime.datetime.now()
mer3 = str((b - a).total_seconds())
print(f'Частично отсортированный слиянием = {mer3}')


#Вставка отсортированных массивов
j = 0
for i in range(len(array)):
    if array[i] is None:
        array[i] = Sort[j]
        j += 1

print(array)

