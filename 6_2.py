from prettytable import PrettyTable
#Инициализация узла
class Node:

    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    #Добавление узла
    def addNode(self, data):
        #Если значение больше, то в левую часть
        if self.value > data:
            if self.left:
                return self.left.addNode(data)
            else:
                self.left = Node(data)
                self.left.parent = self.value
        #Если значение меньше или равно, то в правую часть
        elif self.value < data:
            if self.right:
                return self.right.addNode(data)
            else:
                self.right = Node(data)
                self.right.parent = self.value

        else:
            if self.right:
                return self.right.addNode(data)
            else:
                self.right = Node(data)
                return True

    #Вывод узла
    def preOrder(self):
        print(self.value)
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()


class Tree:

    def __init__(self):
        self.root = None

    def addNode(self, data):
        if self.root:
            return self.root.addNode(data)
        else:
            self.root = Node(data)

    #Удаление узла
    def remove(self, data):

        if self.root is None:
            return False
        #Перебор допустимых вариантов и в зависимости от состояния сдвиг значения
        elif self.root.value == data:
            if self.root.left is None and self.root.right is None:
                self.root = None

            elif self.root.left and self.root.right is None:
                self.root = self.root.left

            elif self.root.left is None and self.root.right:
                self.root = self.root.right
            #Присваивание "родителю" корня и сдвиг узла
            elif self.root.left and self.root.right:
                delNodeParent = self.root
                delNode = self.root.right
                while delNode.left:
                    delNodeParent = delNode
                    delNode = delNode.left

                self.root.value = delNode.value
                if delNode.right:
                    if delNodeParent.value > delNode.value:
                        delNodeParent.left = delNode.right
                    elif delNodeParent.value < delNode.value:
                        delNodeParent.right = delNode.right
                else:
                    if delNode.value < delNodeParent.value:
                        delNodeParent.left = None
                    else:
                        delNodeParent.right = None

            return True

        parent = None
        node = self.root

        while node and node.value != data:
            parent = node
            node.parent = parent
            if data < node.value:
                node = node.left
            elif data > node.value:
                node = node.right
        #Перебор допустимых вариантов значений узла и корня, в зависимости от состояния сдвиг значения узла и родителя
        if node is None or node.value != data:
            return False

        elif node.left is None and node.right is None:
            if data < parent.value:
                parent.left = None
            else:
                parent.right = None

        elif node.left and node.right is None:
            if data < parent.value:
                parent.left = node.left
            else:
                parent.right = node.left

        elif node.left is None and node.right:
            if data < parent.value:
                parent.left = node.right
            else:
                parent.right = node.right

        else:
            delNodeParent = node
            delNode = node.right
            while delNode.left:
                delNodeParent = delNode
                delNode = delNode.left

            node.value = delNode.value
            if delNode.right:
                if delNodeParent.value > delNode.value:
                    delNodeParent.left = delNode.right
                elif delNodeParent.value < delNode.value:
                    delNodeParent.right = delNode.right
            else:
                if delNode.value < delNodeParent.value:
                    delNodeParent.left = None
                else:
                    delNodeParent.right = None

    def preOrder(self):
        if self.root is not None:
            print("Дерево =>")
            self.root.preOrder()
        else:
            print('Значения в дереве отсутствуют')

t = PrettyTable()

th = ["Пункт"]
td = ["1. добавить узел в дерево" ,
      "2. удалить узел из дерева" ,
      "3. вывести содержимое узлов" ]
columns = len(th)
table = PrettyTable(th)

td_data = td[:]

while td_data:
    table.add_row(td_data[:columns])
    td_data = td_data[columns:]
print(table)

tree = Tree()
tree.addNode(11)
tree.addNode(71)
tree.addNode(156)
tree.addNode(92)
tree.addNode(13)
tree.addNode(1)

while True:
    x = int(input('Введите команду: '))
    if x == 1:
        N = int(input('Введите значение узла: '))
        tree.addNode(N)
    elif x == 2:
        N = int(input('Введите значение узла: '))
        tree.remove(N)
    elif x == 3:
        tree.preOrder()
    elif x == 4:
        break
    else:
        print('Такой команды нет')
