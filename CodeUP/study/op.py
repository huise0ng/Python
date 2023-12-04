class ArrayStack:
    def __init__(self, stack_size=5):
        self.stack_size = stack_size
        self.list = [None] * stack_size
        self.top = -1

    def isEmpty(self):  
        return self.top == -1

    
    def isFull(self): 
        return self.top == self.stack_size - 1

    def push(self, e):

        if self.isFull():
            print("스택이 가득찼습니다.")
        else:
            self.top = self.top + 1
            self.list[self.top] = e

    def pop(self):  
        if self.isEmpty():
            print("스택이 비어있습니다.")
        else:
            self.top = self.top - 1
            return self.list[self.top + 1]

    def peek(self):  
        if self.isEmpty():
            print("스택이 비어있습니다.")
        else:
            return self.list[self.top]



def precedence(op):
    if op == '*' or op == '/':
        return 2 
    elif op == '+' or op == '-':
        return 1  
    elif op == '(' or op == ')':
        return 0  
    else:
        return -1 


def Infix2Postfix(expr):
    s = ArrayStack(100)  
    output = []
    for term in expr:  
        if term in '(':  
            s.push('(')  

        elif term in ')': 
            while not s.isEmpty(): 
                op = s.pop()  
                if op == '(': 
                    break  
                else:
                    output.append(op)  

        elif term in '*/+-': 
            while not s.isEmpty(): 
                op = s.peek()      
                if precedence(term) <= precedence(op):    
                    output.append(op)   
                    s.pop()             
                else: break
            s.push(term)    

        else:
            output.append(term)

    while not s.isEmpty():
        output.append(s.pop())

    return output

infix1=input()
infix1=list(infix1)
postfix=Infix2Postfix(infix1)
print(postfix)