'''
Stack implementation.
'''


class Stack:
    def __init__(self, size: int):
        self.elements = [None] * size
        self.size = size
        self.top = -1

    def __repr__(self):
        return f'Stack: {self.elements} | TOP: {self.top}'
    
    def push(self, element: str):
        if self.top == self.size - 1:
            print('Stack Overflow')
            return None
        self.top += 1
        self.elements[self.top] = element
    
    def pop(self): 
        if self.top == -1:
            return 'Stack Underflow'
        value = self.elements[self.top]
        self.elements[self.top] = None
        self.top -= 1
        return value
    
    def peek(self): 
        if self.top == -1:
            return 'Stack Underflow'
        value = self.elements[self.top]
        return value



# Test
# test_stack = Stack(5)
# print(test_stack)

# test_stack.push('A')
# print(test_stack)
# test_stack.push('B')
# print(test_stack)
# test_stack.push('C')
# print(test_stack)
# test_stack.push('D')
# print(test_stack)
# test_stack.push('E')
# print(test_stack)
# test_stack.push('F')
# print(test_stack)

# print(test_stack.pop())
# # test_stack.push('F')
# print(test_stack)
# print(test_stack.pop())
# print(test_stack)
# print(test_stack.pop())
# print(test_stack)
# print(test_stack.pop())
# print(test_stack)
# print(test_stack.pop())
# print(test_stack)
# print(test_stack.pop())
# print(test_stack)
