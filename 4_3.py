#Чтение строки из файла
f = open("4_3.txt","r")
wInt = f.read().split()
hash = {}
count = -1

print("Введите число для поиска = ")
NumberSearch = int(input())

#Преобразование строки в числа
for i in range(len(wInt)):
    wInt[i] = int(wInt[i])

#Добавление ключей
keys = []
for i in range(11):
    keys.append(str(i))

hash = dict.fromkeys(keys)
for i in range(len(keys)):
    if keys[i] in hash:
       hash[keys[i]] = []

#Добавление значений в таблицу
for i in range(len(wInt)):
    ost = str(wInt[i] % 11)
    hash[ost].append(wInt[i])

print(hash)

#Поиск числа
for i in range(len(hash)):
    ord = str(i)
    for j in range(len(hash[ord])):
        count += 1
        if NumberSearch == hash[ord][j]:
            print(f'count = {count}')
            quit()

