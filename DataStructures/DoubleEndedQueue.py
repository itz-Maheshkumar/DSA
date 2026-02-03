from collections import deque
class DoubleEndedQueue:
    def __init__(self):
        self.deque = deque()

    def insert_front(self, value):
        self.deque.appendleft(value)

    def insert_rear(self, value):
        self.deque.append(value)

    def delete_front(self):
        if not self.deque:
            return "Deque Empty"
        return self.deque.popleft()

    def delete_rear(self):
        if not self.deque:
            return "Deque Empty"
        return self.deque.pop()

    def display(self):
        return list(self.deque)
    
dq = DoubleEndedQueue()
dq.insert_front(10)
dq.insert_rear(20)
dq.delete_front()
dq.insert_rear(30)
print(dq.display())