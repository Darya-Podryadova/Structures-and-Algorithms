class Node: #Инициализация
    def __init__(self, item = None, next = None):
        self.next = next
        self.item = item
    def __str__(self):
        return f'Item = {self.item}'

class FIFO:
    def __init__(self): #Инициализация
        self.first = None
        self.last =None
        self.max = -1
        self.min = 100000000
        self.posmax = 0
        self.posmin = 0
        self.count = 0

    def push(self): #Добавление элемента
        print("Enter number = ")
        item =int(input())
        if self.first == None:
            self.last = self.first = Node(item, None)
        else:
            self.last.next = self.last = Node(item, None)


    def iterate(self): #Последовательная итерация
        node = self.first
        while (node):
            print(node.item)
            node = node.next

    def minmax(self): #Определение максимального и минимального элемента и их позиций
        k = -1
        node = self.first
        if (self.max == -1) :
            while (node):
                k += 1
                if self.max < node.item:
                    self.max = node.item
                    self.posmax = k
                if (self.min == node.item) or (self.min > node.item):
                    self.min = node.item
                    self.posmin = k
                node = node.next
        print("min = "+str(self.min)+"  позиция мин = "+str(self.posmin)+"   max = "+str(self.max)+" позиция макс = "+str(self.posmax))
        return self.posmin, self.posmax

    def pop(self, i): #Удаление элемента с определенного места
        if (self.first == None):
            return
        old = curr = self.first
        count = 0
        if i == 0:
            self.first = self.first.next
            return
        while curr != None:
            if count == i:
                if curr.next == self.last:
                    self.last = curr
                    break
                else:
                    old.next = curr.next
                break
            old = curr
            curr = curr.next
            count += 1

a = FIFO()
print("Enter N = ")
N = int(input())
while N != 0:
    a.push()
    N -= 1
a.iterate()
pin, pax = a.minmax() #Присваивание значений позиций вне класса
if pin < pax: #Удаление элемента между максимальным и минимальным
    for i in range(pax - pin ):
        a.pop(pin+1)
else:
    for i in range(pin - pax ):
        a.pop(pax+1)
#a.pop(2)
print("result =")
a.iterate() #Вывод результата

