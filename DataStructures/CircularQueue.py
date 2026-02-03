class CircularQueue:
    def __init__(self, k):
        self.size = k
        self.queue = [None]*k
        self.front = self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            return "Queue Full"
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value

    def dequeue(self):
        if self.front == -1:
            return "Queue Empty"
        data = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return data

    def display(self):
        if self.front == -1:
            return []
        if self.rear >= self.front:
            return self.queue[self.front:self.rear+1]
        return self.queue[self.front:] + self.queue[:self.rear+1]
    
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.dequeue()
print(cq.display())
