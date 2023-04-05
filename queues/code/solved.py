class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class Queue:
    def __init__(self):
        self.front = self.rear = None
 
    def is_empty(self):
        return self.front == None
 
    def enqueue(self, data):
        new_node = Node(data)
 
        if self.rear == None:
            self.front = self.rear = new_node
            return
 
        self.rear.next = new_node
        self.rear = new_node
 
    def dequeue(self):
        if self.is_empty():
            return None
 
        temp = self.front
        self.front = temp.next
 
        if(self.front == None):
            self.rear = None
        return str(temp.data)


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue()) # prints 1
print(q.dequeue()) # prints 2
print(q.dequeue()) # prints 3
print(q.dequeue()) # prints None