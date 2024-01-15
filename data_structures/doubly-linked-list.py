#Node constructor for doubly linked list

class Node:
    def __init__(self, value): 
        self.value = value
        self.next = None
        self.prev = None

# Doubly linked list constructor 
class DoublyLinkedList: 
    def __init__(self, value): 
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head == None: 
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1 
        # Insert method requires boolean return 
        return True 
    
    def pop(self):
        # If no items in linked list
        if self.length == 0:
            return None
        # Set temp variable to tail 
        temp = self.tail
        # If 1 item in linked list 
        if self.length == 1: 
            self.head = None
            self.tail = None
        else: 
            # Move pointer to previous node
            self.tail = self.tail.prev
            # Set next node to none to remove end node
            self.tail.next = None 
            # Break off temp pointer
            temp.prev = None 
        self.length -= 1
        return temp 
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1
        return True 

            
my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.append(8)
my_doubly_linked_list.pop()
my_doubly_linked_list.prepend(5)

my_doubly_linked_list.print_list()