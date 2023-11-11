class CircularQueue:
    def __init__(self, capacity=5):
        self.list = [None]*capacity
        self.fornt =0
        self.rear = 0
              
    def isEmpty(self) :             
        return self.front == self.rear
    
    def isFull(self) :
        return self.front == (self.rear + 1)
    
    def enqueue(self,item):
        if not self.isFull():
            self.rear = (self.rear + 1)
            self.items[self.rear] = item
            
            
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1)
            return self.items[self.front]