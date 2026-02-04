class StackList:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]

s = StackList()
s.push(10)
s.push(20)
s.push(30)

print(s.peek())
print(s.pop())
print(s.pop())