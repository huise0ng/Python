class Stack:
    def __init__(self, size):
        self.stack = [None] * size
        self.top = -1
        self.size = size

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def push(self, element):
        if not self.is_full():
            self.top += 1
            self.stack[self.top] = element
            print(self.stack)
        else:
            print("Stack overflow")

    def pop(self):
        if not self.is_empty():
            popped_element = self.stack[self.top]
            self.top -= 1
            return popped_element
        else:
            print("Stack underflow")

    def peek(self):
        if not self.is_empty():
            return self.stack[self.top]


stack_size = 5
stack = Stack(stack_size)

stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
