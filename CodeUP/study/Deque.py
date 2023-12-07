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
        return (self.rear + 1) % self.cap == self.front

    def enQueue(self, item):
        if self.isFull():
            print("Stack Overflow")
            exit()
        else:
            self.rear = (self.rear + 1) % self.cap
            self.list[self.rear] = item

    def deQueue(self):
        if self.isEmpty():
            exit()
        else:
            self.front = (self.front + 1) % self.cap
            self.list[self.front]

    def addRear(self, item):
        if self.isFull():
            exit()
        else:
            self.rear = (self.rear + 1) % self.cap
            self.list[self.rear] = item

    def deleteRear(self):
        if self.isEmpty():
            exit()
        else:
            removed_item = self.list[self.rear]
            self.list[self.rear] 
            self.rear = (self.rear - 1) % self.cap
            return removed_item

    def getRear(self):
        if self.isEmpty():
            exit()
        else:
            return self.list[self.rear]

    def printQueue(self):
        for i in range(self.cap):
            print(self.list[i], end=" ")

a = Queue(5)
a.addRear(15)
a.addRear(13)
a.addRear(11)
a.addRear(10)

print(a.getRear()) 

a.deleteRear()  
a.deleteRear()  

print(a.getRear()) 

a.printQueue()  
