from collections import deque

class StackDeque:
    def __init__(self):
        self.stack = deque()
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]

s = StackDeque()
s.push("a")
s.push("b")
s.push("c")

print(s.peek())
print(s.pop())
print(s.pop())