class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
 
    def is_empty(self):
        return self.head is None
 
    def append(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
 
    def prepend(self, data):
        node = Node(data)
        if self.is_empty():
            self.tail = node
        else:
            node.next = self.head
        self.head = node
 
    def includes(self, data):
        if self.is_empty():
            return False
 
        if self.head.data == data:
            return True
 
        curr = self.head.next
        while True:
            if curr.data == data:
                return True
            if curr.next == None:
                return False
            curr = curr.next
 
    def __str__(self):
        if self.is_empty():
            return "[]"
 
        node = self.head
        nodes = [str(node.data)]
        while node.next is not None:
            node = node.next
            nodes.append(str(node.data))
        return "[" + "->".join(nodes) + "]"




linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
print(linked_list.includes(0)) # prints False
linked_list.prepend(0)
print(linked_list.includes(0)) # prints True