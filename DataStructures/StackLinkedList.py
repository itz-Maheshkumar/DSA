class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node
    def pop(self):
        value = self.top.data
        self.top = self.top.next
        return value
    def peek(self):
        return self.top.data

s = StackLinkedList()
s.push(100)
s.push(200)
s.push(300)

print(s.peek())
print(s.pop())
print(s.pop())
