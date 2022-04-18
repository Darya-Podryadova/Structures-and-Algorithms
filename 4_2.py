def HASH (hash,word):

    wordASCII = word[::1]

    for i in range(len(word)):
        wordASCII[i] = list(wordASCII[i])

    b = 0
    count = []

    #Преобразование символа в число, согласно таблице ASCII
    for i in range(len(wordASCII)):
        for j in range(len(wordASCII[i])):
            wordASCII[i][j] = ord(wordASCII[i][j])
            b += int(wordASCII[i][j])
        count.append(b)
        b = 0

    for i in range(len(keys)):
        if keys[i] in hash:
            hash[keys[i]] = []

    #Заполнение таблицы словами, используя метод остатков
    for i in range(len(wordASCII)):
        ost = str(count[i] % n)
        hash[ost].append(word[i])

    return hash

f = open("4_2.txt","r")
word = f.read().split()

hash = {}
wordASCII = []
wordFORdelete = word[::1]

print("Введите размерность таблицы = ")
n = int(input())

print("Введите букву = ")
letter = str(input())

print("Введите слово для поиска  = ")
wordSearch = str(input())
count = -1

#Заполнение хэш-таблицы введенным значением
keys =[]
for i in range(n):
    keys.append(str(i))
hash = dict.fromkeys(keys)

k = 0
#Подсчет количества слов, которые нужно удалить
for i in range(len(wordFORdelete)):
    if letter == wordFORdelete[i][0]: k+=1

for i in range(len(wordFORdelete) - k ):
   if letter == wordFORdelete[i][0]:
       del wordFORdelete[i]
       i -= 1



print(HASH(hash,word))
print(HASH(hash,wordFORdelete))

search = HASH(hash, word)

#Поиск слова
for i in range(len(search)):
    ord = str(i)
    for j in range(len(search[ord])):
        count += 1
        if wordSearch == search[ord][j]:
            print(f'count = {count}')
            quit()

