# Node constructor
class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

# Linked list constructor 
class LinkedList:
    def __init__(self, value): 
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

# Print items in linked list
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

    def pop(self):
        if self.length == 0: 
            return None
        temp = self.head
        pre = self.head 
        # While temp.next is not None
        while(temp.next): 
            pre = temp 
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        # Second if statement is after length is decremented
        if self.length == 0:
            self.head = None
            self.tail = None
        # Return node that was just removed
        # For testing, return temp.value 
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        # Use temp: head needs something pointing at it in order to remove
        temp = self.head 
        self.head = self.head.next 
        temp.next = None
        self.length -= 1
        # Second if statement after decrementer, when starting with one item
        if self.length == 0:
            self.tail = None
        # Return item removed from linked list 
        return temp 

my_linked_list = LinkedList(2)

# Add 3 to end of list
my_linked_list.append(3)

my_linked_list.prepend(1)

my_linked_list.print_list()

# Test cases for pop()
'''
# Test (2) Items - Returns 2 Node
print(my_linked_list.pop())
# Test (1) Item - Returns 1 Node
print(my_linked_list.pop())
# Test (0) Items - Returns None
print(my_linked_list.pop())
'''

# Test cases for pop_first()
'''
# Test (2) Items - Returns 2 Node
print(my_linked_list.pop_first())
# Test (1) Item - Returns 1 Node
print(my_linked_list.pop_first())
# Test (0) Items - Returns None
print(my_linked_list.pop_first())
'''

