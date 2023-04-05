class Queue:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return len(self.items) == 0
 
    def enqueue(self, data):
        self.items.append(data)
 
    def dequeue(self):
        if self.is_empty():
            return None
 
        return self.items.pop()


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue()) # prints 1
print(q.dequeue()) # prints 2
print(q.dequeue()) # prints 3   
print(q.dequeue()) # prints None