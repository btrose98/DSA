class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, data):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)

        # Case: list is empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        current_node = self.head
        current_node.prev = new_node
        new_node.next = current_node
        self.head = new_node

    def insert_at_end(self, data):
        # Case: list is empty
        if not self.head:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        current_node = self.tail

        current_node.next = new_node
        new_node.prev = current_node
        self.tail = new_node

    def insert_at_index(self, index, data):
        if index == 0:
            self.insert_at_beginning(data)
            return

        position = 0
        current_node = self.head
        previous_node = None
        while current_node and position != index:
            position += 1
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            if position == index:
                self.insert_at_end(data)
            else:
                print("index out of bounds")
            return

        new_node = Node(data)
        previous_node.next = new_node
        new_node.prev = previous_node
        new_node.next = current_node
        current_node.prev = new_node

    def delete_by_value(self, value):
        if not self.head:
            print("empty list")
            return

        current_node = self.head
        if current_node.data == value:
            self.head = current_node.next

        previous_node = current_node.prev
        while current_node:
            if current_node.data == value:
                previous_node.next = current_node.next
                current_node.next.prev = previous_node

            previous_node = current_node
            current_node = current_node.next

    def delete_at_index(self, index):
        if not self.head:
            print("list is empty")
            return

        current_node = self.head
        if index == 0:
            self.head = current_node.next

        previous_node = current_node.prev
        position = 0
        while current_node and position != index:
            previous_node = current_node
            current_node = current_node.next
            position += 1

        if not current_node:
            print("index out of bounds")
            return

        # position == index
        previous_node.next = current_node.next
        current_node.next.prev = current_node.prev


    def __repr__(self):
        if not self.head:
            return "The list is empty"

        linked_list_string = ""
        current_node = self.head
        while current_node:
            linked_list_string += f"{current_node.data} -> "
            current_node = current_node.next
        linked_list_string += "None"
        return linked_list_string


data = [1, 2, 3, 4, 326243, 35, 6, 23, 6, 7]
linked_list = DoublyLinkedList(None)
for val in data:
    linked_list.insert_at_end(val)
print(linked_list)


# linked_list.insert_at_index(7, 97)
# print(linked_list)

linked_list.delete_at_index(2)
print(linked_list)