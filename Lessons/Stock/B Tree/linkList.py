# Create example link list class to store value and next node

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create a linked list class
class LinkedList:
    def __init__(self):
        self.head = None

    # Add a new node to the linked list
    def add_node(self, value):
        new_node = Node(value)
        new_node.next = None
        if self.head is None:
            self.head = new_node  # If the list is empty, the new node becomes the head.
        else:
            current = self.head
            while current.next:
                current = current.next  # Traverse to the last node.
            current.next = new_node  # Link the last node to the new node.

    # Print the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

# Example usage:
linked_list = LinkedList()
linked_list.add_node(30)
linked_list.add_node(15)
linked_list.add_node(7)
linked_list.print_list()
