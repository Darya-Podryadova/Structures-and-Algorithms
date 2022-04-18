from random import randint

""" Создание списка,
 его сортировка по возрастанию
и вывод на экран"""
a = []
b = []
for i in range(30000):
    a.append(randint(-1000, 1000))
#print(a)
a.sort()
#print(a)

# искомое число
print("Введите искомое число =")
value = int(input())
# Середина, левая и правая границы
mid = len(a) // 2
low = 0
high = len(a) - 1
k = 0

while a[mid] != value and low <= high:
    if value > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("No value")
else:

    for i in range(len(a)):
        if a[i] == value:
            b.append(i)
            k += 1
    print("ID =", b )
    print("Колво = ", k)
