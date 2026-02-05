class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, val):
        if val < self.data:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BST(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BST(val)

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data and self.left:
            return self.left.search(val)
        if val > self.data and self.right:
            return self.right.search(val)
        return False

    def find_min(self):
        curr = self
        while curr.left:
            curr = curr.left
        return curr

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if not self.left:
                return self.right
            if not self.right:
                return self.left
            temp = self.right.find_min()
            self.data = temp.data
            self.right = self.right.delete(temp.data)
        return self

root = BST(50)
for x in [30, 70, 20, 40, 60, 80]:
    root.insert(x)

print(root.search(40))
root = root.delete(50)
print(root.search(50))
