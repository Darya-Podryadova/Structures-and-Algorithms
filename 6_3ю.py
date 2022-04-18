print("Enter word = ")
t = str(input())
S = set()
M = len(t)
d = {}

#Создание шаблона требуемого слова
for i in range(M-2, -1, -1):
    if t[i] not in S:
        d[t[i]] = M-i-1
        S.add(t[i])

if t[M-1] not in S:
    d[t[M-1]] = M

d['*']  = M

#Запись в файл и чтение из него
f = open('test.txt',"w")
f.write("there is a word dog in this sentence   my  cat loves mice")
f.close()
f = open('test.txt',"r")
a = f.read()

N = len(a)

#Проход по строке, накладывая шаблон, пока слово не найдется
if N >= M:
    i = M-1
    while(i < N):
        k = 0
        for j in range(M-1,-1,-1):
            if a[i-k] != t[j]:
                if j == M-1:
                    off = d[a[i]] if d.get(a[i], False) else d['*']
                else:
                    off = d[t[j]]

                i += off
                break
            k += 1
        if j == 0:
            print(f'слово найдено по индексу {i-k+1}')
            break
else:
    print("слова нет")