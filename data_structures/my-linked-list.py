# Node constructor
class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

# Linked List constructor 
class LinkedList:
    def __init__(self, value): 
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

# Print List
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

# Append item to end of linked list
    def append(self, value):
        new_node = Node(value)
        # Test to see if linked list is empty 
        if self.head is None:
            self.head = new_node
            self.tail = new_node 
        else: 
            self.tail.next = new_node
            self.tail = new_node
        # Increase length of linked list by 1
        self.length += 1     

my_linked_list = LinkedList(1)

my_linked_list.append(2)

my_linked_list.print_list()


