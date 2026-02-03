class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.queue:
            return "Queue Empty"
        return self.queue.pop(0)

    def peek(self):
        if not self.queue:
            return "Queue Empty"
        return self.queue[0]

    def display(self):
        return self.queue

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()
print(q.display())
print("Front element:", q.peek())