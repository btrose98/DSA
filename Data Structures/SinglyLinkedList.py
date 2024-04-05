class SinglyLinkedListNode:
    def __init__(self, data):
        self.head = None
        # self.tail = None
        self.data = data
        self.next = None

    def insert_at_beginning(self, data):
        new_node = SinglyLinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_index(self, data, index):
        if index == 0:
            self.insert_at_beginning(data)
            return

        position = 0
        current_node = self.head
        while current_node is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            new_node = SinglyLinkedListNode(data)
            new_node.next = current_node.next
            current_node.next = new_node
            return

        print("Index not present")

    def insert_at_end(self, data):
        new_node = SinglyLinkedListNode(data)

        # case: empty linked list
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def delete_by_value(self, data):
        if not self.head:
            return

        previous_node = None
        current_node = self.head
        while current_node.next:
            if current_node.data == data:
                if previous_node:
                    previous_node.next = current_node.next
                else:   # This is the head of the linked list
                    self.head = current_node.next

            previous_node = current_node
            current_node = current_node.next

    def delete_at_index(self, index):
        if not self.head:
            return

        # Case: replacing index 0 (head)
        current_node = self.head
        if index == 0:
            self.head = current_node.next
            return

        previous_node = None
        position = 0
        while current_node.next:
            if position == index:
                previous_node.next = current_node.next

            previous_node = current_node
            current_node = current_node.next
            position += 1

    def __repr__(self):
        linked_list_str = ""
        current_node = self.head
        while current_node is not None:
            linked_list_str += str(current_node.data) + " -> "
            current_node = current_node.next
        linked_list_str += "None"
        return linked_list_str


data = [1, 2, 3, 4, 326243, 35, 6, 23, 6, 7]
linked_list = SinglyLinkedListNode(None)
for val in data:
    linked_list.insert_at_end(val)

print(linked_list)

# linked_list.delete_by_value(1)
linked_list.delete_at_index(1)
print(linked_list)
