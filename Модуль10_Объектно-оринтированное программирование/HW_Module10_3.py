# Реализация класса узла для двусвязного списка
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None  # ссылка на следующий узел
        self.prev = None  # ссылка на предыдущий узел


# Класс двусвязного списка
class DoubleLinkedList:
    def __init__(self):
        self.head = None  # первый узел списка
        self.tail = None  # последний узел списка

    # Добавляет новый узел в конец списка
    def append(self, data):
        new_node = DNode(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # Удаляет узел с заданным значением
    def delete(self, value):
        current = self.head

        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                print(f'Элемент {value} удалён')
                return True

            current = current.next

        print(f'Элемент {value} не найден')
        return False

    # Отображает элементы списка вперед (head -> tail)
    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Отображает элементы списка назад (tail -> head)
    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" <- ")
            current = current.prev
        print("None")

    # Проверка наличия значения в списке
    def contains(self, value):
        current = self.head
        while current:
            if current.data == value:
                print(f'Элемент {value} присутствует в списке')
                return True
            current = current.next
        print(f'Элемент {value} отсутствует в списке')
        return False

    # Замена одного значения другим
    def replace(self, old_value, new_value):
        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_value
                print(f'Элемент {old_value} заменён на {new_value}')
                return True
            current = current.next
        print(f'Элемент {old_value} не найден')
        return False


# Тестирование нового класса
double_list = DoubleLinkedList()
double_list.append(1)
double_list.append(2)
double_list.append(3)

print("Отображение вперёд:")
double_list.display_forward()  # 1 -> 2 -> 3 -> None

print("\nОтображение назад:")
double_list.display_backward()  # 3 <- 2 <- 1 <- None

double_list.contains(2)  # Элемент 2 присутствует в списке
double_list.contains(4)  # Элемент 4 отсутствует в списке

double_list.delete(2)  # Элемент 2 удалён
double_list.display_forward()  # 1 -> 3 -> None

double_list.replace(1, 10)  # Элемент 1 заменён на 10
double_list.display_forward()  # 10 -> 3 -> None