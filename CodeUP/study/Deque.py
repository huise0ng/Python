class Queue:
    def __init__(self, cap=5):
        self.cap = cap
        self.list = [0] * cap
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        if self.rear == self.front:
            return True
        else:
            return False

    def isFull(self):
        return (self.rear + 1)%self.cap == self.rear

    def enQueue(self, item):
        if self.isFull():
            print("Stack Overflow")
            exit()
        else:
            self.rear =(self.rear+1) % self.cap
            self.list[self.rear] = item

    def deQueue(self):
        if self.isEmpty():
            print("Stack Underflow")
            exit()
        else:
            self.front =(self.front+1) % self.cap
            self.list[self.front] = None


    def printQueue(self):
        for i in range(self.cap):
            print(self.list[i],end=" ")

a = Queue(5)
a.enQueue(15)
a.enQueue(13)
a.enQueue(11)
a.enQueue(10)
a.deQueue()
a.deQueue()
print()
a.printQueue()
