'''
Queue implementation
'''


class Queue:
    def __init__(self, size: int):
        self.elements = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1

    def __repr__(self): 
        return f'\nQueue: {self.elements} | F: {self.front} R: {self.rear}'
    
    def enqueue(self, element: str):
        if self.rear == self.size - 1:
            print('\nQueue overflow')
            return
        if self.rear == -1 and self.front == -1:
            self.rear = 0
            self.front = 0
        else:
            self.rear += 1
        self.elements[self.rear] = element
        
    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print('\nQueue underflow')
            return
        else:
            value = self.elements[self.front]
            self.elements[self.front] = None
            self.front += 1
            return value



# Test
q = Queue(5)
print(q)

# Enqueues
q.enqueue('A')
print(q)
q.enqueue('B')
print(q)
q.enqueue('C')
print(q)
# q.enqueue('D')
# print(q)
# q.enqueue('E')
# print(q)
# q.enqueue('F') # Overflow test
# print(q)

# Dequeues
print(f'\nReturned: {q.dequeue()}')
print(q)
print(f'\nReturned: {q.dequeue()}')
print(q)
print(f'\nReturned: {q.dequeue()}')
print(q)
# print(f'\nReturned: {q.dequeue()}')
# print(q)
# print(f'\nReturned: {q.dequeue()}')
# print(q)
# print(f'\nReturned: {q.dequeue()}')
# print(q)


q.enqueue('F')
print(q)
q.enqueue('G')
print(q)
q.enqueue('H')
print(q)
