class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def __repr__(self):
        return str(self.value)


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.current = head
        self.tail = head
        self.length = 0

    def append(self, new_element):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_element
            new_element.previous = current
            self.tail = new_element
        else:
            self.head = new_element
            self.tail = new_element

    def get_position(self, position):
        current = self.head
        if position < 1:
            return None
        while current and position > 1:
            current = current.next
            position -= 1
        return current

    def insert(self, new_element, position):
        if position == 1:
            new_element.next = self.head
            if self.head:
                self.head.previous = new_element
            self.head = new_element
            if not self.tail:
                self.tail = new_element
        else:
            current = self.get_position(position)
            if current:
                new_element.next = current
                new_element.previous = current.previous
                if current.previous:
                    current.previous.next = new_element
                current.previous = new_element
            else:
                self.append(new_element)

    def delete(self, value):
        current = self.head
        while current and current.value != value:
            current = current.next
        if current:
            if current.previous:
                current.previous.next = current.next
            else:
                self.head = current.next
            if current.next:
                current.next.previous = current.previous
            else:
                self.tail = current.previous
            current = None

    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next


linked_list_of_fruits = LinkedList()

element1 = Node("banana")
element2 = Node("mango")
element3 = Node("grapes")
element4 = Node("pineapple")
element5 = Node("apple")
element6 = Node("blueberry")

linked_list_of_fruits.append(element1)
linked_list_of_fruits.append(element2)
linked_list_of_fruits.append(element3)
linked_list_of_fruits.append(element4)
linked_list_of_fruits.append(element5)
linked_list_of_fruits.append(element6)
linked_list_of_fruits.print_list()
